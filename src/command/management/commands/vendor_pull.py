from django.core.management.base import BaseCommand
from typing import Any
import helpers

from django.conf import settings

VENDOR_DIR=getattr(settings,'VENDOR_DIR')


VENDOR_STATICFILES = {

   "flowbite.min.css": "https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.css",
    "flowbite.min.js": "https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.js",
    "flowbite.min.js.map": "https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.js.map"

}

class Command(BaseCommand):
    #entry point
    def handle(self, *args: Any, **options: Any) -> None:
        download=[]
        self.stdout.write("Downloading vendor static files......")
        for name,url in VENDOR_STATICFILES.items():
            dest_path=VENDOR_DIR/name
            dl_success=helpers.download_to_local(url,dest_path)
            if dl_success:
                download.append(url)

            else:
                self.stdout.write("failed to download  files...")
        if len(download)==len(VENDOR_STATICFILES):
            self.stdout.write("All files downloaded successfully")
        else:
            self.stdout.write("Some files failed to download")
