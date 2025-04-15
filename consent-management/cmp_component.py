import edgee_world.consent_management.exports as exports
import edgee_world.consent_management.exports.consent_management as consent_management

from edgee_world.consent_management.types import *

class ConsentManagement(exports.ConsentManagement):
    def map(self, cookies: List[Tuple[str, str]], settings: List[Tuple[str, str]]) -> Optional[consent_management.Consent]:
        cookies_dict = dict(cookies)
        settings_dict = dict(settings)

        key = cookies_dict.get("key")
        if key is None:
            return None

        if key == "granted":
            return consent_management.Consent.GRANTED
        elif key == "denied":
            return consent_management.Consent.DENIED
        else:
            return consent_management.Consent.PENDING


        raise NotImplementedError
