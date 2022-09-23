import os
from templateframework.metadata import Metadata

def run(metadata: Metadata = None):

    path_arq = f"{metadata.inputs['application_path']}.java"

    with open(path_arq,'r') as f:
              
    return metadata