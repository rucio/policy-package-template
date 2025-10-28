SUPPORTED_VERSION = [">=35.0.0"] # Specify the Rucio versions supported by this policy package

def get_algorithms():
    from yourvo_rucio_policy_package.non_deterministic_pfn import YourVONonDeterministicPFNAlgorithm
    from yourvo_rucio_policy_package.scope import YourVOScopeExtractionAlgorithm
    from yourvo_rucio_policy_package.lfn2pfn import YourVORSEDeterministicTranslation
    return { 
        'non_deterministic_pfn': {
            'yourvo_non_deterministic_pfn': YourVONonDeterministicPFNAlgorithm.construct_non_deterministic_pfn_yourvo
            },
         'lfn2pfn': {
             'yourvo_lfn2pfn': YourVORSEDeterministicTranslation.lfn2pfn_yourvo
             },
         'scope': { 
             'yourvo_extract_scope': YourVOScopeExtractionAlgorithm.extract_scope_yourvo
             } 
    }