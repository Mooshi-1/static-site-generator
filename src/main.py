import os
import shutil

from copystatic import copy_files_recursive
from gencontent import generate_pages_recursive, generate_page


dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating content...")
    #generate_page(dir_path_static, template_path, dir_path_public)
    # print("Generating content...")
    generate_pages_recursive(
         dir_path_content,  # from_path: the markdown file
         template_path,                    # template_path: the HTML template
         dir_path_public   # dest_path: where to save the generated HTML
)
    #generate_pages_recursive(dir_path_content, template_path, dir_path_public)


main()
