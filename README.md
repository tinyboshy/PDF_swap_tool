# PDF_swap_tool

## Usage
### 1. clone repo
```
git clone https://github.com/tinyboshy/PDF_swap_tool.git
```
### 2. Place the pdf file in the same hierarchy as swap.py
### 3. edit parameter
- Number of pages in the pdf file
- Number of first and last pages to swap
- Path of the pdf file
### 4. Build docker container and run
```
docker-compose run --rm pdf_swap
```