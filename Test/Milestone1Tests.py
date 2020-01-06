import pytest
import transactions as txn
from objectifier import Objectifier
import json
from filehash import FileHash
from uuid import uuid4

config = Objectifier(json.load(open('Test/testconfig.json')))

class TestMilestone1():

    #envsetup
    def test_one(self):
        """
            Delete all the files on the server
        """
        files = txn.list_available_files().json()
        for items in files:
            rs = txn.delete_a_file_by_id(items['id'])
            assert(rs.status_code==200)

    # Verify that when there are no files, the list call displays no results
    def test_two(self):
        """
        Verify that the list Files returns no files when there are no files to be displayed
        """
        response = txn.list_available_files().json()
        assert(response.__len__()==0)
    

    # Verify that a file can be uploaded successfully 
    def test_three(self):
        """
        Verify that the a file can be uploaded successfully
        """
        response = txn.upload_a_file(config.TEST_DATA.test_three.file_to_upload)
        assert(response.status_code==200)


    # Verify that the uploaded file can be reterived sucessfully - Verify check sum
    def test_four(self):
        """
        Verify that the uploaded file can be reterived sucessfully - Verify check sum before upload and after reterive
        """
        md5= FileHash('sha1')
        hash = md5.hash_file(config.TEST_DATA.test_four.file_to_upload)
        response = txn.upload_a_file(config.TEST_DATA.test_four.file_to_upload)
        assert(response.status_code==200)
        id = response.text
        r = txn.retrive_a_file_by_id(id)       
        open(config.TEST_DATA.test_four.file_name, 'wb+').write(r.content)
        hash_2 = md5.hash_file(config.TEST_DATA.test_four.file_name)
        assert(hash==hash_2)

    # Verify that when there are files , the list call displays the files correctly 
    def test_five(self):
        """
        Verify that when there are files , the list call displays the files correctly 
        """
        count = txn.list_available_files().json()
        assert(count.__len__()>0)

    # Verify that a delete operation happens successfully
    def test_six(self):
        """
        Verify that a delete operation happens successfully
        """
        response = txn.upload_a_file(config.TEST_DATA.test_five.file_to_upload)
        assert(response.status_code==200)
        id = response.text
        r = txn.retrive_a_file_by_id(id)  
        assert(r.status_code==200)
        delete= txn.delete_a_file_by_id(id)
        assert(delete.status_code==200)
        r = txn.retrive_a_file_by_id(id)
        assert(r.status_code==404)
        list_of_files = txn.list_available_files().json()
        assert(str(id) not in str(list_of_files))
    


    # Verify that appopriate error message is displayed while trying to access a file that doesnt exist
    def test_seven(self):
        """
        Verify that appopriate error message is displayed while trying to access a file that doesnt exist
        """
        r = txn.retrive_a_file_by_id(str(uuid4()))  
        assert(r.status_code==404)

    # Verify that a file can be retrived by name
    def test_eight(self):
        """
        Verify that a file can be retrived by name
        """
        md5= FileHash('sha1')
        hash = md5.hash_file(config.TEST_DATA.test_eight.file_to_upload)
        response = txn.upload_a_file(config.TEST_DATA.test_eight.file_to_upload)
        assert(response.status_code==200)
        rs = txn.reterive_a_file_by_name(config.TEST_DATA.test_eight.file_name)
        assert(rs.status_code==200)
        open(config.TEST_DATA.test_eight.file_name, 'wb+').write(rs.content)
        hash_2 = md5.hash_file(config.TEST_DATA.test_eight.file_name)
        assert(hash==hash_2)


    # Verify that a file can be deleted by name
    def test_nine(self):
        """
        Verify that a file can be deleted by name
        """
        response = txn.upload_a_file(config.TEST_DATA.test_nine.file_to_upload)
        assert(response.status_code==200)
        rs = txn.delete_a_file_by_name(config.TEST_DATA.test_nine.file_name)
        assert(rs.status_code==200)
        
    
    # Verify that an error is returned while trying to upload a duplicate file
    def test_ten(self):
        """
            Verify that an error is returned while trying to upload a duplicate file
        """
        response = txn.upload_a_file(config.TEST_DATA.test_ten.file_to_upload)
        assert(response.status_code==200)
        response = txn.upload_a_file(config.TEST_DATA.test_ten.file_to_upload)
        assert(response.status_code==409)
    
        # Verify that files of various names are accepted during upload
    def test_eleven(self):
        """
        Verify that files of various names are accepted during upload
        """
        file_names = list(config.TEST_DATA.test_eleven.file_names)
        for items in file_names:
            open("Test/TestData/"+items,'w+')
            upload_stat = txn.upload_a_file("Test/TestData/"+items)
            assert(upload_stat.status_code==200)
        list_of_files = txn.list_available_files().json()
        
        file_names_Actual=[]
        for files in list_of_files:
            file_names_Actual.append(files['file_name'])
        assert(txn.is_slice_in_list(file_names,file_names_Actual) , True)
    
    # Verify that appropriate error is retured while trying to delete a file that is not present
    def test_twelve(self):
        """
        Verify that 404 is returned while trying to delete a file that does not exist
        """
        response = txn.upload_a_file(config.TEST_DATA.test_twelve.file_to_upload)
        assert(response.status_code==200)
        id = response.text
        response = txn.delete_a_file_by_id(id)
        assert(response.status_code==200)
        response = txn.delete_a_file_by_id(id)
        assert(response.status_code==404)