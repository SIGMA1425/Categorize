from glob import glob
import os
from bs4 import BeautifulSoup
import json
from tqdm import tqdm

with open("content.jl", "w") as writer:
    for file_path in tqdm(glob("./articles/*/*")):

        dir_path = os.path.dirname(file_path)

        with open(file_path) as fp:
            soup = BeautifulSoup(fp.read())
            title = soup.select_one(".ArticleHeader_headline").text.strip()
            body = soup.select_one(".StandardArticleBody_body").text.strip()
            category = os.path.basename(dir_path)

            json_content = json.dumps({
                "title":title,
                "body":body,
                "category":category,
            }, ensure_ascii=False)

            writer.write(json_content + "\n")