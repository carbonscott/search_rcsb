#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Example:
from search_rcsb import searchMacromolecule

searchMacromolecule('adrenergic receptor')
searchMacromolecule('rhodopsin')
'''

import requests
from urllib.parse import quote

def parseRequest(query, viewOnline = False):
    # The base url to request a query...
    BASE = "https://search.rcsb.org/rcsbsearch/v1/query"
    BASE_replace = "https://www.rcsb.org/search?request="

    # Form the url...
    # Convert to double quote (%22) from single quote (%27) 
    # Convert to "False" from "false"
    query_string = quote(f'{query}').replace("%27", "%22").replace("%22false%22", "false")
    url = f'{BASE}?json={query_string}'

    # Request...
    r = requests.get( url = url )

    if viewOnline: 
        # Request...
        print("Copy and paste the following link to your web browser:")
        print("")
        r = requests.get( url = url )

        # Display the URL for visualizing results in web browser...
        print(r.url.replace(f"{BASE}?json=", BASE_replace))
        print("")
        print("done")

    return r




# [[[ Utilities ]]]
def findSimilarStructure(pdb_entry, viewOnline = True):
    # The query to search similar assemblies...
    query = {
      "query": {
            "type": "terminal",
            "service": "structure",
            "parameters": {
              "value": {
                "entry_id": f"{pdb_entry}",
                "assembly_id": "1"
              },
              "operator": "strict_shape_match"
          }
      },
      "request_options": {
            "pager": {
              "start": 0,
              "rows": 20000,
            }
      },
      "return_type": "assembly"
    }

    r = parseRequest(query, viewOnline = viewOnline)
    return r




def findSimilarSequence(sequence, identity_cutoff, evalue_cutoff = 10, viewOnline = False):
    ''' The E-value The expect value(E-value) can be changed in order to limit
        the number of hits to the most significant ones. The lower the E-value, the
        better the hit. The E-value is dependent on the length of the query
        sequence and the size of the database. For example, an alignment obtaining
        an E-value of 0.05 means that there is a 5 in 100 chance of occurring by
        chance alone.

        E-values are very dependent on the query sequence length and the database size.
        Short identical sequence may have a high E-value and may be regarded as "false
        positive" hits. This is often seen if one searches for short primer regions,
        small domain regions etc. The default threshold for the E-value on the BLAST
        web page is 10. Increasing this value will most likely generate more hits.
        Below are some rules of thumb which can be used as a guide but should be
        considered with common sense.

        - E-value < 10e-100 Identical sequences. You will get long alignments
          across the entire query and hit sequence.
        - 10e-100 < E-value < 10e-50 Almost identical sequences. A long stretch
          of the query protein is matched to the database.
        - 10e-50 < E-value < 10e-10 Closely related sequences, could be a
          domain match or similar.
        - 10e-10 < E-value < 1 Could be a true homologue but it is a gray area.
        - E-value > 1 Proteins are most likely not related
        - E-value > 10 Hits are most likely junk unless the query sequence is
          very short.

        Reference: http://resources.qiagenbioinformatics.com/manuals/clcgenomicsworkbench/650/_E_value.html
    '''
    query = {
      "query": {
        "type": "terminal",
        "service": "sequence",
        "parameters": {
          "evalue_cutoff": evalue_cutoff,
          "identity_cutoff": identity_cutoff/100.0,
          "target": "pdb_protein_sequence",
          "value": sequence
        }
      },
      "return_type": "entry",
      "request_options": {
        "pager": {
          "start": 0,
          "rows": 10000
        },
        "scoring_strategy": "sequence",
        "sort": [
          {
            "sort_by": "score",
            "direction": "desc"
          }
        ]
      }
    }

    r = parseRequest(query, viewOnline = viewOnline)
    return r




def searchMacromolecule(macromolecule_type, viewOnline = False):
    query = {
      "query": {
        "type": "terminal",
        "service": "text",
        "parameters": {
          "operator": "contains_phrase",
          "negation": "false",
          "value": f"{macromolecule_type}",
          "attribute": "rcsb_polymer_entity.pdbx_description"
        }
      },
      "return_type": "entry",
      "request_options": {
        "pager": {
          "start": 0,
          "rows": 1000000
        },
        "scoring_strategy": "combined",
        "sort": [
          {
            "sort_by": "score",
            "direction": "desc"
          }
        ]
      }
    }

    r = parseRequest(query, viewOnline = viewOnline)
    return r
