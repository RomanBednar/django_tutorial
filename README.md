```git clone https://github.com/RomanBednar/django_tutorial```

```cd django_tutorial```

```virtualenv -p python3 --no-site-packages --distribute . && source ./bin/activate && pip install -r requirements.txt```

```
cat > .gitignore << EOF
*  
!README.md  
!requirements.txt   
!mysite/*  
EOF  
```
