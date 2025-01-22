import edgee_world.data_collection.exports as exports
import edgee_world.data_collection.exports.provider as provider

from edgee_world.data_collection.types import *

'''
This is the main class that you will need to implement. It should inherit from
edgee_world.data_collection.exports.Provider and implement the following methods:
page, track, user
'''
class Provider(exports.Provider):
    '''
        The page method should return an EdgeeRequest object that contains the
        information needed to make an HTTP request to the provider's API to
        send page data, passing the event information formatted for the provider's API as well as the credentials
        needed to authenticate with the provider's API.
    '''
    def page(self, e: provider.Event, cred: List[Tuple[str, str]]) -> provider.EdgeeRequest:
        '''
        cred is a list of tuple, which contains each key and secret for the provider
        for example, if your component is set to use
            [[components.data_collection]]
            name = "my_component"
            component = "outpout.wasm"
            credentials.test_project_id = "123456789"
            credentials.test_write_key = "abcdefg"

            cred will be [("test_project_id", "123456789"), ("test_write_key", "abcdefg")]
        '''
        '''
            the function should return the following:
            return provider.EdgeeRequest(
                method=provider.HttpMethod.GET,
                url="https://yourwebsite.com",
                headers={},
                body="")
        '''
        raise NotImplementedError("page is not implemented")

    '''
        The track method should return an EdgeeRequest object that contains the
        information needed to make an HTTP request to the provider's API to
        send track data, passing the event information formatted for the provider's API as well as the credentials
        needed to authenticate with the provider's API.
    '''
    def track(self, e: provider.Event, cred: List[Tuple[str, str]]) -> provider.EdgeeRequest:
        raise NotImplementedError("track is not implemented")

    '''
        The user method should return an EdgeeRequest object that contains the
        information needed to make an HTTP request to the provider's API to
        send user data, passing the event information formatted for the provider's API as well as the credentials
        needed to authenticate with the provider's API.
    '''
    def user(self, e: provider.Event, cred: List[Tuple[str, str]]) -> provider.EdgeeRequest:
        raise NotImplementedError("user is not implemented")
