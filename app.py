"""Madlibs Stories."""
from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story 
# from module stories import story method

app = Flask (__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)

class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


# story = Story(
#     ["place", "noun", "verb", "adjective", "plural_noun"],
#     """Once upon a time in a long-ago {place}, there lived a
#        large {adjective} {noun}. It loved to {verb} {plural_noun}."""
# )


@app.route("/home")
def ask_questions():
    '''Return home page''' 
    prompts = story.prompts 
    # from story class grab prompts = words? 
    return render_template("questions.html", prompts=prompts)


# solution if you hard code the form  (home.html) and pull from there
# @app.route("/story")
# def story():
#     '''Gathers the place, noun, verb, adj, and plural noun from home.html input'''

#     place = request.args["place"]
#     noun = request.args["noun"]
#     verb = request.args["verb"]
#     adjective = request.args["adjective"]
#     plural_noun = request.args["plural_noun"]

#     answers= {
#     place,
#     noun,
#     verb,
#     adjective,
#     plural_noun
#     }

#     return render_template("story.html", place = place, noun = noun, verb = verb, adjective = adjective, plural_noun = plural_noun)

@app.route("/story")
def show_story():
    '''Show full story with pompt answers'''
    text = story.generate("story.html", text=text)
