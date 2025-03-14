import os
import shutil
import requests

LICENSE_URLS = {
    "MIT": "https://raw.githubusercontent.com/spdx/license-list-data/main/text/MIT.txt",
    "GPL-3.0": "https://www.gnu.org/licenses/gpl-3.0.txt",
    "BSD-3-Clause": "https://raw.githubusercontent.com/spdx/license-list-data/main/text/BSD-3-Clause.txt",
    "Apache-2.0": "https://raw.githubusercontent.com/spdx/license-list-data/main/text/Apache-2.0.txt",
    "Unlicense": None,
    "Proprietary": None,
    "Custom": None,
}

def download_license(url, destination_path):
    """Downloads a license file from a URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(destination_path, "wb") as f:
            f.write(response.content)
        print(f"Downloaded license from {url} to LICENSE")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading license from {url}: {e}")
        # Create a placeholder file even if download fails
        with open(destination_path, "w") as f:
            f.write(f"*** DOWNLOAD FAILED:  License from {url} ***\n")
            f.write("*** Please replace this with the correct license text. ***\n")
        print(f"Created placeholder LICENSE file due to download failure.")

def create_placeholder_license(license_name, destination_path):
    """Creates a placeholder license file with example content."""
    if license_name == "Unlicense":
        content = """
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org/>
"""
    elif license_name == "Proprietary":
        content = """
PROPRIETARY LICENSE

Copyright (c) [Year] [Your Name or Company Name]

All rights reserved.

This software is the confidential and proprietary information of [Your Name or Company Name] ("Confidential Information"). You shall not
disclose such Confidential Information and shall use it only in accordance
with the terms of the license agreement you entered into with [Your Name or Company Name].

This software is provided "AS IS" without warranty of any kind, either express or implied, including but not limited to the implied warranties of merchantability and fitness for a particular purpose.  [Your Name or Company Name] shall not be liable for any damages suffered by you as a result of using, modifying or distributing this software or its derivatives.

UNAUTHORIZED REPRODUCTION OR DISTRIBUTION OF THIS SOFTWARE, OR ANY PORTION OF IT, MAY RESULT IN SEVERE CIVIL AND CRIMINAL PENALTIES, AND WILL BE PROSECUTED TO THE MAXIMUM EXTENT POSSIBLE UNDER THE LAW.

---

[Add any other specific terms and conditions here.]
"""
    elif license_name == "Custom":
        content = """
CUSTOM LICENSE

This software is licensed under a custom license agreement.  Please refer to the
separate license agreement document provided with this software for the full
terms and conditions.

---

[Add a brief description of the key terms here, or instructions on where to find the full license.]

---

[Example: You might say something like "This software is free to use for non-commercial purposes, but requires a paid license for commercial use.  See the LICENSE.md file for details."]
"""
    else:  # Should not happen, but good practice to have a default
        content = f"*** UNKNOWN LICENSE: {license_name} ***\nPlease replace this with the correct license text."

    with open(destination_path, "w") as f:
        f.write(content)
    print(f"Created placeholder LICENSE file for {license_name}")

def copy_license_file():
    """Handles license file creation (download or placeholder)."""
    chosen_license = "{{ cookiecutter.license }}"
    destination_path = "LICENSE"

    if chosen_license in ("Unlicense", "Proprietary", "Custom"):
        create_placeholder_license(chosen_license, destination_path)
    else:
        license_url = LICENSE_URLS.get(chosen_license)
        if license_url:
            download_license(license_url, destination_path)
        else:
            print(f"Warning: Unknown license choice '{chosen_license}'.")

if __name__ == "__main__":
    copy_license_file()