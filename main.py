from copy_files import *
from save_paths import  *
import streamlit as st
import time

file_types_dict = {
    'Text': ['.txt', '.csv'],
    'Image': ['.jpg', '.png', '.gif'],
    'Document': ['.doc', '.docx', '.pdf']}

if __name__ == "__main__":
    start_time = time.time()
    directory_to_search = "F:/CODES/ORCA/From Github/Fake_Image_Detector/TurboCopySearch/Validation/Real"
    destination_folder = 'F:/CODES/ORCA/From Github/Fake_Image_Detector/TurboCopySearch/Validation'
    file_type = st.selectbox("What kind of files are you looking for?", ("Image", "Document","Text"))
    file_types={file_type:file_types_dict[file_type]}
    directory_to_search = st.text_input('Path to folder:')
    destination_folder = st.text_input('Path to destination folder:')
    # if st.button('Browse'):
    #     dialog = wx.DirDialog(None, 'Selecta folder:', style = wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
    #     if dialog.ShowModal() == wx.ID_OK:
    #         folder_path = dialog.GetPath()
    batch_size = 20000
    txt_file_folder = f"{destination_folder}/txt_folder"
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    os.makedirs(txt_file_folder, exist_ok=True)

    st.write('WELCOME TO DIJITA TECHNOLOGIES TCS App')

    if st.button('Run Turbo Copy'):
        st.write("Your copy process has started")
        st.write(f"Retrieving path of all {file_type} in the source folder...")
        group_and_save_files(directory_to_search, file_types, txt_file_folder, batch_size)
        copy_files_from_text_files(txt_file_folder, destination_folder, max_workers=4)
        st.write(f"Task finished. All {file_type} have been copied | Total time: {round((time.time() -start_time)/60,2)} minutes ")