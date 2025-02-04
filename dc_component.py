import edgee_world.data_collection.exports as exports
import edgee_world.data_collection.exports.data_collection as data_collection

from edgee_world.data_collection.types import *

'''
This is the main class that you will need to implement. It should inherit from
edgee_world.data_collection.exports.Provider and implement the following methods:
page, track, user
'''
class DataCollection(exports.DataCollection):
    '''
        The page method should return an EdgeeRequest object that contains the
        information needed to make an HTTP request to the provider's API to
        send page data, passing the event information formatted for the provider's API as well as the settings
        needed to authenticate with the provider's API.
    '''
    def page(self, e: data_collection.Event, settings: List[Tuple[str, str]]) -> data_collection.EdgeeRequest:
        '''
        settings is a list of tuple, which contains each key and secret for the provider
        for example, if your component is set to use
            [[components.data_collection]]
            name = "my_component"
            component = "outpout.wasm"
            settings.test_project_id = "123456789"
            settings.test_write_key = "abcdefg"

            settings will be [("test_project_id", "123456789"), ("test_write_key", "abcdefg")]
        '''
        '''
            the function should return the following:
            return provider.EdgeeRequest(
                method=provider.HttpMethod.GET,
                url="https://yourwebsite.com",
                headers={},
                forward_client_headers=true,
                body="")
        '''
        raise NotImplementedError("page is not implemented")

    '''
        The track method should return an EdgeeRequest object that contains the
        information needed to make an HTTP request to the provider's API to
        send track data, passing the event information formatted for the provider's API as well as the settings
        needed to authenticate with the provider's API.
    '''
    def track(self, e: data_collection.Event, settings: List[Tuple[str, str]]) -> data_collection.EdgeeRequest:
        raise NotImplementedError("track is not implemented")

    '''
        The user method should return an EdgeeRequest object that contains the
        information needed to make an HTTP request to the provider's API to
        send user data, passing the event information formatted for the provider's API as well as the settings
        needed to authenticate with the provider's API.
    '''
    def user(self, e: data_collection.Event, settings: List[Tuple[str, str]]) -> data_collection.EdgeeRequest:
        raise NotImplementedError("user is not implemented")
