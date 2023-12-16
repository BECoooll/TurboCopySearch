from copy_files import *
from save_paths import  *
import streamlit as st
import time

file_types_dict = {
    'Text': ['.txt', '.csv'],
    'Image': ['.jpg', '.png', '.gif'],
    'Document': ['.doc', '.docx', '.pdf']}

if __name__ == "__main__":
    st.write('WELCOME TO DIJITA TECHNOLOGIES AppStore')

    start_time = time.time()
    directory_to_search = "F:/CODES/ORCA/From Github/Fake_Image_Detector/TurboCopySearch/Validation/Real"
    destination_folder = 'F:/CODES/ORCA/From Github/Fake_Image_Detector/TurboCopySearch/Validation'
    file_type = st.selectbox("What kind of files are you looking for?", ("Image", "Document","Text"))
    file_types={file_type:file_types_dict[file_type]}

    directory_to_search = st.session_state.get("Path_to_source", None)
    folder_select_button = st.button("Select Source Folder")
    if folder_select_button:
        directory_to_search = select_folder()
        st.session_state.Path_to_source = directory_to_search

    destination_folder = st.session_state.get("Path_to_destination", None)
    folder_select_button = st.button("Select Destination Folder")
    if folder_select_button:
        destination_folder = select_folder()
        st.session_state.Path_to_destination = destination_folder

    batch_size = 20000
    txt_file_folder = f"{destination_folder}/txt_folder"
    os.makedirs(txt_file_folder, exist_ok=True)


    if st.button('Run Turbo Copy'):
        st.write("Your copy process has started")
        st.write(f"Retrieving path of all {file_type} in the source folder...")
        group_and_save_files(directory_to_search, file_types, txt_file_folder, batch_size)
        copy_files_from_text_files(txt_file_folder, destination_folder, max_workers=4)
        st.write(f"Task finished. All {file_type} have been copied | Total time: {round((time.time() -start_time)/60,2)} minutes ")