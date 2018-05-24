#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 24 18:30:30 2018

@author: pt
"""

import os, sys
import zipfile
import wget
import time


self_all_gids = []


class AutoDownloader(object):
    
    def __init__(self, project_dir, data_to_download):     
        os.chdir(project_dir)
           
        download_common_utils(project_dir)
        from PyAria2 import PyAria2 ###############################################################???
        import utils ###############################################################???
           
        downloader = PyAria2()   
        __add_files_to_aria(downloader, project_dir, data_to_download)                
        printDownloadStatus(downloader)

        print('\n Unzipping') 
        unzip_all(project_dir, data_to_download)
        
        print('\n ############## Downloading Complete ##############')

       
    
    def download_common_utils(project_dir):
        os.chdir(project_dir)
        print('Confirm the current working directory: ')
        print(project_dir)
        
        common_utils_dir = project_dir + '/COMMON_UTILS'
        
        if not os.path.isdir(common_utils_dir):    
            os.mkdir(common_utils_dir)
            os.chdir(common_utils_dir)
        
            aria_url = 'https://raw.githubusercontent.com/zhenlohuang/pyaria2/master/pyaria2.py'
            utils_url = 'https://raw.githubusercontent.com/algorithmica-repository/deep-learning/master/2018-feb/common_utils/utils.py'
            wget.download(aria_url , out = 'PyAria2.py')
            wget.download(utils_url , out = 'utils.py')
        else:
            print('/COMMON_UTILS already exists')
        sys.path.insert(0, common_utils_dir)   
        
        
        
        
        ###############################################################
    def __download_url(downloader,directory, url):    
        os.chdir(directory)
        global_download_options = downloader.getGlobalOption()
        global_download_options['max-connection-per-server'] = '16'
        downloader.changeGlobalOption(global_download_options)
        print(type(url))
        gid=downloader.addUri([url], {'dir':directory})
        self_all_gids.append(gid)


   
    def unzip_all(project_dir, data_to_download):
        for directory, url_links in data_to_download.items():        
            full_path_directory = project_dir + directory
            unzip_individual_directory(full_path_directory)
    
    
    
    def unzip_individual_directory(full_path_directory):    
        print('Unzipping items in '+ full_path_directory)
        extension = ".zip"
    
        for item in os.listdir(full_path_directory):
            print('file is: ' + item)
            if item.endswith(extension): # check for ".zip" extension
                file_name = full_path_directory + '/' + item # get full path of files
                
                print('File to unzip: '+file_name)
                zip_ref = zipfile.ZipFile(file_name) # create zipfile object
                zip_ref.extractall(full_path_directory) # extract file to dir
                zip_ref.close() # close file
                os.remove(file_name) # delete zipped file



    ################################################
    def printDownloadStatus(downloader):
        
        while downloader.tellActive():    
            print('>>>>>>>>>>>>>>>>>')
            for item in self_all_gids:        
                status = downloader.tellStatus(item)
                
                if status['status'] == 'active':              
                    completedLength = float(status['completedLength'])
                    totalLength = float(status['totalLength'])
                    
                    if not totalLength == 0:                
                        percentage_completed = (completedLength / totalLength) * 100
                        percentage_completed = round(percentage_completed, 2) 
                    else:
                        print('Waiting for file size')
                        percentage_completed = completedLength
                                    
                    speed = int(status['downloadSpeed']) /(1024*1024) 
                    speed = round(speed, 2)
              
                    temp = status['files'][0]
                    temp = temp['uris']
                    temp = temp[0]
                    url = temp['uri']
                    
                    print('Url: ' + url)        
                    print('Completed: ' + str(percentage_completed) + '%' + '     Speed: '+ str(speed) + ' MBps' + '     Total Connections: ' + status['connections'])
                    print('\n')                  
            time.sleep(2)               
        downloader.shutdown() 
 


def __add_files_to_aria(downloader, project_dir, data_to_download):    
    for directory, url_links in data_to_download.items():
        full_path_directory = project_dir + directory
        if os.path.isdir(full_path_directory):
            print('Data previously downloaded at: ' + full_path_directory)
        else:         
            print('>>>Creating directory: '+ full_path_directory )
            print(type(url_links))
            os.makedirs(full_path_directory)
            
            for url in url_links:
                __download_url(downloader,full_path_directory, url) 



    












