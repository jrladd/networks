book :
	jupyter-book build --all .
	git add -A
	git commit -am "rebuilding book"
	git push
	ghp-import -n -p -f _build/html