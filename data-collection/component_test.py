import unittest
from edgee_world.data_collection.exports.data_collection import *
from edgee_world.data_collection.types import *
from dc_component import DataCollection

class TestDataCollection(unittest.TestCase):
    def setUp(self):
        self.event_page = Event(
            uuid="1b3e639b-e222-4d15-90b4-5ecec3fe809b",
            timestamp=1737631094,
            timestamp_millis=1737631094989,
            timestamp_micros=1737631094989242,
            event_type=EventType.PAGE,
            data=Data_Page(
                value=PageData(
                    name="",
                    category="",
                    keywords=["demo", "tag manager"],
                    title="Page with Edgee components",
                    url="https://demo.edgee.app/analytics-with-edgee.html",
                    path="/analytics-with-edgee.html",
                    search="",
                    referrer="https://demo.edgee.dev/analytics-with-edgee.html",
                    properties=[]
                )
            ),
            context=Context(
                page=PageData(
                    name="",
                    category="",
                    keywords=["demo", "tag manager"],
                    title="Page with Edgee components",
                    url="https://demo.edgee.app/analytics-with-edgee.html",
                    path="/analytics-with-edgee.html",
                    search="",
                    referrer="https://demo.edgee.dev/analytics-with-edgee.html",
                    properties=[]
                ),
                user=UserData(
                    user_id="",
                    anonymous_id="",
                    edgee_id="d3640e27-a7fd-4940-8ad7-21794454f506",
                    properties=[]
                ),
                client=Client(
                    ip="127.0.0.0",
                    locale="en-us",
                    timezone="Europe/Paris",
                    user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
                    user_agent_architecture="x86",
                    user_agent_bitness="64",
                    user_agent_version_list="Not A(Brand;8|Chromium;132",
                    user_agent_full_version_list="Not A(Brand;8.0.0.0|Chromium;132.0.6834.83",
                    user_agent_mobile="0",
                    user_agent_model="",
                    os_name="Linux",
                    os_version="6.6.71",
                    screen_width=1920,
                    screen_height=1280,
                    screen_density=1.5,
                    continent="",
                    country_code="",
                    country_name="",
                    region="",
                    city=""
                ),
                campaign=Campaign(
                    name="",
                    source="",
                    medium="",
                    term="",
                    content="",
                    creative_format="",
                    marketing_tactic=""
                ),
                session=Session(
                    session_id="1737629837",
                    previous_session_id="",
                    session_count=3,
                    session_start=False,
                    first_seen=1737536678,
                    last_seen=1737631094
                )
            ),
            consent=Consent.PENDING
        )

        self.event_track = Event(
            uuid="8b995883-e5ec-42ab-a6ac-74c3f5468f4b",
            timestamp=1737631444,
            timestamp_millis=1737631444650,
            timestamp_micros=1737631444650964,
            event_type=EventType.TRACK,
            data=Data_Track(
                value=TrackData(
                    name="button_click",
                    properties=[
                        ("label", "Blue Sneakers"),
                        ("registered", "false"),
                        ("color", "blue"),
                        ("category", "shoes"),
                        ("size", "10")
                    ],
                    products=[]
                )
            ),
            context=Context(
                page=PageData(
                    name="",
                    category="",
                    keywords=["demo", "tag manager"],
                    title="Page with Edgee components",
                    url="https://demo.edgee.app/analytics-with-edgee.html",
                    path="/analytics-with-edgee.html",
                    search="",
                    referrer="https://demo.edgee.dev/analytics-with-edgee.html",
                    properties=[]
                ),
                user=UserData(
                    user_id="",
                    anonymous_id="",
                    edgee_id="d3640e27-a7fd-4940-8ad7-21794454f506",
                    properties=[]
                ),
                client=Client(
                    ip="127.0.0.0",
                    locale="en-us",
                    timezone="Europe/Paris",
                    user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
                    user_agent_architecture="x86",
                    user_agent_bitness="64",
                    user_agent_version_list="Not A(Brand;8|Chromium;132",
                    user_agent_full_version_list="Not A(Brand;8.0.0.0|Chromium;132.0.6834.83",
                    user_agent_mobile="0",
                    user_agent_model="",
                    os_name="Linux",
                    os_version="6.6.71",
                    screen_width=1920,
                    screen_height=1280,
                    screen_density=1.5,
                    continent="",
                    country_code="",
                    country_name="",
                    region="",
                    city=""
                ),
                campaign=Campaign(
                    name="",
                    source="",
                    medium="",
                    term="",
                    content="",
                    creative_format="",
                    marketing_tactic=""
                ),
                session=Session(
                    session_id="1737629837",
                    previous_session_id="",
                    session_count=3,
                    session_start=False,
                    first_seen=1737536678,
                    last_seen=1737631444
                )
            ),
            consent=Consent.PENDING
        )

        self.event_user = Event(
            uuid="55ab2462-81f3-4993-9a24-d98f2d01c5d1",
            timestamp=1737631604,
            timestamp_millis=1737631604611,
            timestamp_micros=1737631604611036,
            event_type=EventType.USER,
            data=Data_User(
                value=UserData(
                    user_id="123456",
                    anonymous_id="anon-123",
                    edgee_id="d3640e27-a7fd-4940-8ad7-21794454f506",
                    properties=[
                        ("name", "John Doe"),
                        ("email", "me@example.com"),
                        ("age", "42"),
                        ("verified", "true")
                    ]
                )
            ),
            context=Context(
                page=PageData(
                    name="",
                    category="",
                    keywords=["demo", "tag manager"],
                    title="Page with Edgee components",
                    url="https://demo.edgee.app/analytics-with-edgee.html",
                    path="/analytics-with-edgee.html",
                    search="",
                    referrer="https://demo.edgee.dev/analytics-with-edgee.html",
                    properties=[]
                ),
                user=UserData(
                    user_id="",
                    anonymous_id="",
                    edgee_id="d3640e27-a7fd-4940-8ad7-21794454f506",
                    properties=[]
                ),
                client=Client(
                    ip="127.0.0.0",
                    locale="en-us",
                    timezone="Europe/Paris",
                    user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
                    user_agent_architecture="x86",
                    user_agent_bitness="64",
                    user_agent_version_list="Not A(Brand;8|Chromium;132",
                    user_agent_full_version_list="Not A(Brand;8.0.0.0|Chromium;132.0.6834.83",
                    user_agent_mobile="0",
                    user_agent_model="",
                    os_name="Linux",
                    os_version="6.6.71",
                    screen_width=1920,
                    screen_height=1280,
                    screen_density=1.5,
                    continent="",
                    country_code="",
                    country_name="",
                    region="",
                    city=""
                ),
                campaign=Campaign(
                    name="",
                    source="",
                    medium="",
                    term="",
                    content="",
                    creative_format="",
                    marketing_tactic=""
                ),
                session=Session(
                    session_id="1737629837",
                    previous_session_id="",
                    session_count=3,
                    session_start=False,
                    first_seen=1737536678,
                    last_seen=1737631604
                )
            ),
            consent=Consent.PENDING
        )

        # Set up mock credentials
        self.credentials = [("test_project_id", "123456789"), ("test_write_key", "abcdefg")]
        # Instantiate the DataCollection class
        self.data_collection = DataCollection()

    def test_page_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            self.data_collection.page(self.event_page, self.credentials)

    def test_track_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            self.data_collection.track(self.event_track, self.credentials)

    def test_user_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            self.data_collection.user(self.event_user, self.credentials)

if __name__ == "__main__":
    unittest.main()

