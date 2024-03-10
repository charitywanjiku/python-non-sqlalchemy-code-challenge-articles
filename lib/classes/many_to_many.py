class Article:
    all = []  # Class attribute to hold all instances of articles

    def __init__(self, author, magazine, title):
        # Initializing instance attributes
        self.author = author
        self.magazine = magazine
        self._title = str(title)  # Private attribute for title

        Article.all.append(self)  # Adding instance to the class attribute list

    @property
    def title(self):
        # Getter property for title
        return self._title

    @title.setter
    def title(self, title):
        return self.title
        # Setter property for title, raising AttributeError if someone tries to change it
        raise AttributeError("Title is immutable")


class Author:
    def __init__(self, name):
        # Initializing instance attribute for name
        self._name = name

    @property
    def name(self):
        # Getter property for name
        return self._name

    @name.setter
    def name(self, new_names):
        # Setter property for name
        self.new_names = new_names
        return self._name

    def articles(self):
        # Method to get articles authored by this author
        return [articles for articles in Article.all if articles.author == self]

    def magazines(self):
        # Method to get magazines this author has written for
        return list(set([article.magazine for article in self.articles()]))

    def add_article(self, magazine, title):
        # Method to add new article authored by this author
        articles = Article(self, magazine, title)
        return articles

    def topic_areas(self):
        # Method to get topic areas covered by this author
        return list(set([article.magazine.category for article in self.articles()])) if self.articles() else None

    def contributing_authors(self):
        # Method to get authors who have contributed articles
        return [authors for authors in Author.all if len(authors.articles()) > 0]


class Magazine:
    def __init__(self, name, category):
        # Initializing instance attributes for name and category
        self._name = name
        self._category = category

    @property
    def name(self):
        # Getter property for name
        return self._name

    @property
    def category(self):
        # Getter property for category
        return self._category

    @name.setter
    def name(self, new_names):
        # Setter property for name
        if isinstance(new_names, str):
            if 2 <= len(new_names) <= 16:
                self._name = new_names
        return self._name

    @category.setter
    def category(self, new_categories):
        # Setter property for category
        if isinstance(new_categories, str):
            if len(new_categories) > 0:
                self._category = new_categories
        return self._category

    def articles(self):
        # Method to get articles published in this magazine
        return [articles for articles in Article.all if articles.magazine == self]

    def contributors(self):
        # Method to get authors who have contributed to this magazine
        return list(set([articles.author for articles in self.articles()]))

    def article_titles(self):
        # Method to get titles of articles published in this magazine
        titles = [articles.title for articles in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        # Method to get authors who have contributed more than 2 articles
        authors = {}
        for articles in self.articles():
            if articles.author in authors:
                authors[articles.author] += 1
            else:
                authors[articles.author] = 1
        contributing_authors = [author for author, count in authors.items() if count > 2]
        return contributing_authors if contributing_authors else None
