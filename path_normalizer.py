import re
from urllib.parse import urlparse

UUID_PATTERN = re.compile(r'^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$')
NUMERIC_PATTERN = re.compile(r'^\d+$')
HASH_PATTERN = re.compile(r'^[0-9a-fA-F]{16,64}$')

def normalize_path(full_url: str) -> tuple[str, dict[str, str]]:
    parsed = urlparse(full_url)
    segments = [s for s in parsed.path.split('/') if s]
    
    normalized_segments = []
    extracted_params: dict[str, str] = {}
    
    for idx, seg in enumerate(segments):
        if UUID_PATTERN.match(seg):
            param_name = f"{segments[idx-1]}_id" if idx > 0 else "id"
            normalized_segments.append(f"{{{param_name}}}")
            extracted_params[param_name] = "string (uuid)"
        elif NUMERIC_PATTERN.match(seg):
            param_name = f"{segments[idx-1]}_id" if idx > 0 else "id"
            normalized_segments.append(f"{{{param_name}}}")
            extracted_params[param_name] = "integer"
        elif HASH_PATTERN.match(seg):
            param_name = f"{segments[idx-1]}_hash" if idx > 0 else "hash"
            normalized_segments.append(f"{{{param_name}}}")
            extracted_params[param_name] = "string (hash)"
        else:
            normalized_segments.append(seg)
            
    norm_path = "/" + "/".join(normalized_segments)
    return norm_path, extracted_params
