import re

from mutagen.mp4 import MP4Cover

from enums.image_format import ImageFormat

class FormatHelper:

    def extract_first_consecutive_number_from_string(string: str) -> int | None:
        
        match = re.search(r'\d+', string)

        if match:
            return(int(match.group()))

        return None
    
    def image_bytes_to_mp4_cover(
            image_bytes: bytes,
            image_format: ImageFormat) -> MP4Cover:
        
        mp4_cover_format = None

        if image_format == ImageFormat.JPEG:
            mp4_cover_format = MP4Cover.FORMAT_JPEG
        
        elif image_format == ImageFormat.PNG:
            mp4_cover_format = MP4Cover.FORMAT_PNG
        
        mp4_cover = MP4Cover(image_bytes, mp4_cover_format)

        return mp4_cover
    
    def playlist_url_to_valid_format(playlist_url: str):

        re_match = re.search(r"watch\?(.*?)&", playlist_url)

        invalid_substring: str = re_match.group(1)

        valid_url: str = playlist_url.replace(f"watch?{invalid_substring}", "playlist?")
        
        return valid_url

        
