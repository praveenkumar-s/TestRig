import pytest
import transactions as txn
from objectifier import Objectifier
import json

config = Objectifier(json.load(open('Test/testconfig.json')))
class TestSanityCases():
    def test_Upload(self):
        """
        Verify that Upload of a file works fine
        """
        upload_response = txn.upload_a_file(config.TEST_DATA.sanity_test.file_to_upload)
        assert(upload_response.status_code in [200,201])#, "status code 200 was expected , recieved {0}".format(upload_response.status_code))
                    
    def test_list(self):
        """
        Verify that list operation of files works fine
        """
        list_response = txn.list_available_files()
        assert(config.TEST_DATA.sanity_test.file_name in list_response.text)#, "The uploaded file was not listed on the /upload/list route")

    def test_download(self):
        """
        Verify that Download of a file works fine
        """
        download_response = txn.reterive_a_file_by_name(config.TEST_DATA.sanity_test.file_name)
        assert(download_response.status_code ==200 )#, "status code 200 was required during downlod, but got {0}".format(download_response.status_code))

    def test_delete(self):
        """
        Verify that delete operation works fine
        """
        delete_response = txn.delete_a_file_by_name(config.TEST_DATA.sanity_test.file_name)
        assert(delete_response.status_code ==200 )#, "delete operation must return status code 200, but recieved {0}".format(delete_response.status_code))


