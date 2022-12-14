#START
from math import ceil


class PhotoAlbum:
    photos_per_page = 4
    def __init__(self,pages):
        self.pages = pages

        self.photos = self.build_photos()

    def build_photos(self):
        result = []

        for _ in range(self.pages):
            result.append([])
        return result

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = ceil(photos_count / PhotoAlbum.photos_per_page)
        return cls(pages)

    def add_photo(self, label: str):
        # for page in range(self.pages):
        #     # if len(page) < 4:
        #     #     page.append(label)
        #     #     return f"{label} photo added successfully on page {self.photos.index(page) + 1} slot {len(page)}"
        #     for position in range(PhotoAlbum.photos_per_page):
        #         if self.photos[page][position] is None:
        #             self.photos[page][position] = label
        #             return f"{label} photo added successfully on page {page + 1} slot {position + 1}"

        for row, page in enumerate(self.photos):
            if len(page) < PhotoAlbum.photos_per_page:
                page.append(label)
                return f"{label} photo added successfully on page {row + 1} slot {len(page)}"

        return "No more free slots"

    def display(self):
        delimiter = "-" * 11
        result = delimiter + "\n"

        for page in self.photos:
            # result += f"{' '.join(['[]' for photo in page])}\n"
            # result += "-"*11
            # result += "\n"
            page_str = " ".join(["[]" for photo in page])
            result += page_str + "\n" + delimiter + "\n"

        return result.strip()



album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
