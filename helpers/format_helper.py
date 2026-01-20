import re

class FormatHelper:

    def extract_first_consecutive_number_from_string(string: str) -> int | None:
        
        match = re.search(r'\d+', string)

        if match:
            return(int(match.group()))

        return None
        


