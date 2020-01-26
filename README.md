# TestRig
Validator Test Rig
## Usage: 
  To use the Validator as an standalone executable, Navigate to the root directory of this project and call 
  
  ` RunValidation.exe -e <endpoint url> -t <sanity/milestone1/milestone3>`
  
  Example:
  
  `RunValidation.exe -e http://127.0.0.1:5000 -t sanity -r your_roll_number`
  
  note: do not put a trailing "/" after the url 
 
 ## Configuration:
   Test Configuration is needed for running milestone1 and milestone3 tests. Configuration can be found at:
    
   `Test\testconfig.json`
    
    ```
    {
    "API_SERVER_URL":"http://prsubrama-lt:5000",
    "TEST_DATA":{
        "test_one":{},
        "test_two":{},
        "test_three":{
            "file_to_upload":"Test/TestData/test_file_1.txt"
        },
        "test_four":{
            "file_to_upload":"Test/TestData/test_file_2.txt",
            "file_name":"test_file_2.txt"
        },
        "test_five":{
            "file_to_upload":"Test/TestData/test_file_3.txt"
        },
        "test_eight":{
            "file_to_upload":"Test/TestData/test_file_4.txt",
            "file_name":"test_file_4.txt"
        },
        "test_nine":{
            "file_to_upload":"Test/TestData/test_file_5.txt",
            "file_name":"test_file_5.txt"
        },
        "test_ten":{
            "file_to_upload":"Test/TestData/test_file_6.txt"
        },
        "test_eleven":{
            "file_names":[
                "ABCDEF!@#$%^&().txt",
                "testung with spaces.txt",
                "testing_underscores-data.txt",
                "test.file.name.txt"
            ]
        },
        "test_twelve":{
            "file_to_upload":"Test/TestData/test_file_7.txt"
        },
        "sanity_test":{
            "file_to_upload":"Test/TestData/test_file_1.txt",
            "file_name":"test_file_1.txt"
        }, 
        "milestone_3":{
            "app_config_location":"D:/Users/prsubrama/OneDrive - KLA Corporation/Documents/Praveen/PrivateFoundry/milestone-1/config.json",
            "file_1_path":"Test/TestData/M3_T_K_Test.file",
            "file_2_path":"Test/TestData/M3_2_K_Test_one.file",
            "file_3_path":"Test/TestData/M3_2_K_Test_two.file",
            "location_of_nodes":"D:/Users/prsubrama/OneDrive - KLA Corporation/Documents/Praveen/PrivateFoundry/milestone-1/uploads"
        }
    }
}```

 Make sure to update the *app_config_location* and *location_of_nodes* in the config file
