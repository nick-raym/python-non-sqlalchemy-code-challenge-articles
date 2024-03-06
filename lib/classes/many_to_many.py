class Article:
    all=[]
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        self.addArticle()
        self.author.add_article(magazine,title)
        self.author.add_magazine(magazine)
    
    def addArticle(self):
        self.all.append(self)
    
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self,author):
        if(type(author)==Author):
            self._author=author
        else:
            raise ValueError("Enter valid title")

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self,title):
        if(hasattr(self,"title")):
            raise ValueError("Title already entered")
        elif(type(title)==str and 5<=len(title)<=50):
            self._title = title
        else:
            # pass
            raise ValueError("Enter text with 5-50 letters")
        
class Author:
    
    def __init__(self, name):
        self.name = name
        self.articles=[]
        self.magazines=[]

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        if(hasattr(self,"name")):
            raise ValueError("name already entered")
        elif(type(name)==str):
            if(len(name)>0):
                self._name = name
            else:
                raise ValueError("Enter valid name")
        else:
            raise ValueError("Enter valid name")
        
    @property
    def articles(self):
        return self._articles
    
    @articles.setter
    def articles(self,articles):
        self._articles=articles
    

    def add_magazine(self,magazine):
        if(not magazine in self.magazines):
            self.magazines.append(magazine)

    def add_article(self, magazine, title):
        for e in Article.all:
            if(title==e.title and magazine==e.magazine):
                self.articles.append(e)
                return e
                
            

    def topic_areas(self):
        pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass