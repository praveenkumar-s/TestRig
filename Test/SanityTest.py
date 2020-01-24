import pytest
import transactions as txn
from objectifier import Objectifier
import json
import csv
from datetime import datetime
import os
import socket

config = Objectifier(json.load(open('Test/testconfig.json')))

class TestSanityCases():
    def setup_method(self):
        self.test_suite_name = 'Sanity'
        self.status = 'Fail'

    def test_Upload(self):
        """
        Verify that Upload of a file works fine
        """
        self.test_name = self.test_Upload.__doc__        
        try:
            upload_response = txn.upload_a_file(config.TEST_DATA.sanity_test.file_to_upload)
            assert(upload_response.status_code in [200,201])#, "status code 200 was expected , recieved {0}".format(upload_response.status_code))
            self.status = 'Pass'
        except Exception as e:
            self.status = 'Fail'
            raise e

    def test_list(self):
        """
        Verify that list operation of files works fine
        """
        self.test_name = self.test_list.__doc__        
        try:
            list_response = txn.list_available_files()
            assert(config.TEST_DATA.sanity_test.file_name in list_response.text)#, "The uploaded file was not listed on the /upload/list route")
            self.status = 'Pass'
        except Exception as e:
            self.status = 'Fail'
            raise e

    def test_download(self):
        """
        Verify that Download of a file works fine
        """
        self.test_name = self.test_download.__doc__
        try:
            download_response = txn.reterive_a_file_by_name(config.TEST_DATA.sanity_test.file_name)
            assert(download_response.status_code ==200 )#, "status code 200 was required during downlod, but got {0}".format(download_response.status_code))
        except Exception as e:
            self.status = 'Fail'
            raise e

    def test_delete(self):
        """
        Verify that delete operation works fine
        """
        self.test_name = self.test_delete.__doc__
        try:
            delete_response = txn.delete_a_file_by_name(config.TEST_DATA.sanity_test.file_name)
            assert(delete_response.status_code ==200 )#, "delete operation must return status code 200, but recieved {0}".format(delete_response.status_code))
        except Exception as e:
            self.status = 'Fail'
            raise e

    def teardown_method(self):
        with open(r'Results/ResultStore.csv', 'a', newline='') as csvfile:
            fieldnames = ['Roll_number','Suite','TestCase','Status', 'Ran_at', 'Host_name']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'Roll_number':os.environ.get('ROLL_NUM'), 'Suite':self.test_suite_name,
            'TestCase':self.test_name.replace('\n','') ,
            'Status':self.status, 'Ran_at':str(datetime.now()), 'Host_name':socket.gethostname()})
        