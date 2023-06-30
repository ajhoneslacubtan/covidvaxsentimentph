source = [
    "ako",  # i, me, myself
    "kita",  # we
    "amua",  # our
    "ato",  # ours
    "atoa",  # ourselves
    "ikaw",  # you
    "imong",  # your
    "imo",  # yours
    "akoa",  # -self
    "akong kaugalingon",  # myself
    "kaugalingon",  # -self
    "kamo mismo",  # yourselves
    "siya",  # he, she, him
    "iya",  # his, hers, own
    "kaniya",  # her
    "mismo",  # itself
    "sila",  # they, them
    "ila",  # their
    "ilahang",  # theirs
    "ilang",  # theirs
    "nila",  # them
    "unsa",  # what
    "nga",  # which
    "kinsa",  # who, whom
    "kini",  # this, these
    "kana",  # that
    "mga",  # those
    "kadtong mga",  # those
    "",     # is
    "mga",     # are
    "kaniadto",  # was // kaniadto?
    "niatong",
    # "", # were // kaniadto?
    "mahimong",  # be
    "nahimo",  # been
    "",  # being
    "",  # have
    "",  # has
    "",  # had
    "",  # having
    "",  # do
    "",  # does
    "",  # did
    "",  # doing
    "",  # would
    "",  # should
    "",  # could
    "",  # ought
    "",  # i'm
    "ikaw'ng",  # you're
    "ikaw ang",     # you are
    "",  # he's
    "",  # she's
    "",  # it's
    "kitang",  # we're
    "",  # they're
    "",  # i've
    "",  # you've
    "",  # we've
    "",  # they've
    "",  # i'd
    "",  # you'd
    "",  # he'd
    "",  # she'd
    "",  # we'd
    "",  # they'd
    "",  # i'll
    "",  # you'll
    "",  # he'll
    "",  # she'll
    "",  # we'll
    "",  # they'll
    "",  # isn't
    "",  # aren't
    "",  # wasn't
    "",  # weren't
    "",  # hasn't
    "",  # haven't
    "",  # hadn't
    "",  # doesn't
    "",  # don't
    "",  # didn't
    "",  # won't
    "",  # wouldn't
    "",  # shan't
    "",  # shouldn't
    "",  # can't
    "",  # cannot
    "",  # couldn't
    "",  # mustn't
    "",  # let's
    "",  # that's
    "kinsa'ng",  # who's
    "kinsang",
    "kinsa ang",
    "unsa'ng",  # what's
    "unsa ang",
    "unsang",
    "",  # here's
    "",  # there's
    "kanus-ang",  # when's
    "kanusang",
    "kansang",
    "asang",  # where's
    "nganong",  # why's
    "ngano'ng",
    "giunsa'ng",  # how's
    "ginunsang",
    "ang",  # a
    "",  # an
    "",  # the
    "ug",  # and
    "pero",  # but
    "kung",  # if
    "o",  # or
    "tungod",  # because
    "sama",  # as
    "hangtud",  # until
    "hantud",
    "samtang",  # while
    "",  # of
    "sa",  # at
    "pinaagi",  # by
    "para",  # for
    "uban sa",  # with
    "mahitungod",  # about
    "batok",  # against
    "tali sa",  # between
    "sa",  # into
    "pinaagi sa",  # through
    "samtang",  # during
    "sa panahon",
    "kaniadto",  # before
    "human",  # after
    "itaas",  # above
    "ibabaw",
    "ubos",  # below
    "sa",  # to
    "gikan",  # from
    "taas",  # up
    "ubos",  # down
    "sulod",  # in
    "gawas",  # out
    "",  # on
    "",  # off
    "ibabaw",  # over
    "ilawum",  # under
    "napud",  # again
    "",  # further
    "unya",  # then
    "kas-a",  # once
    "diri",  # here
    "didto",  # there
    "kanus-a",  # when
    "asa",  # where
    "ngano",  # why
    "giunsa",  # how
    "tanan",  # all
    "",  # any
    "",  # both
    "kada",  # each
    "dyutay",  # few
    "pipila",  # few
    "mas",  # more
    "kina",  # most
    "uban",  # other
    "uban pa",  # other
    "",  # some
    "sama",  # such
    "dili",  # no
    "",  # nor
    "",  # not
    "lamang",  # only
    "pareho",  # same
    "busa",  # so
    "kay",  # than
    "pud",  # too
    "kaayo",  # very
]
CEBUANO_STOP_WORDS = frozenset(
    set(source))

TAGALOG_STOP_WORDS = frozenset(["akin", "aking", "ako", "alin", "am", "amin", "aming", "ang", "ano", "anumang", "apat", "at", "atin", "ating", "ay", "bababa", "bago", "bakit", "bawat", "bilang", "dahil", "dalawa", "dapat", "din", "dito", "doon", "gagawin", "gayunman", "ginagawa", "ginawa", "ginawang", "gumawa", "gusto", "habang", "hanggang", "hindi", "huwag", "iba", "ibaba", "ibabaw", "ibig", "ikaw", "ilagay", "ilalim", "ilan", "inyong", "isa", "isang", "itaas", "ito", "iyo", "iyon", "iyong", "ka", "kahit", "kailangan", "kailanman", "kami", "kanila", "kanilang", "kanino", "kanya", "kanyang", "kapag", "kapwa", "karamihan", "katiyakan", "katulad", "kaya", "kaysa", "ko", "kong", "kulang", "kumuha", "kung", "laban", "lahat", "lamang", "likod", "lima", "maaari", "maaaring", "maging", "mahusay", "makita", "marami", "marapat", "masyado", "may", "mayroon", "mga", "minsan", "mismo", "mula", "muli", "na", "nabanggit", "naging", "nagkaroon", "nais", "nakita", "namin", "napaka", "narito", "nasaan", "ng", "ngayon", "ni", "nila", "nilang", "nito", "niya", "niyang", "noon", "o", "pa", "paano", "pababa", "paggawa", "pagitan", "pagkakaroon", "pagkatapos", "palabas", "pamamagitan", "panahon", "pangalawa", "para", "paraan", "pareho", "pataas", "pero", "pumunta", "pumupunta", "sa", "saan", "sabi", "sabihin", "sarili", "sila", "sino", "siya", "tatlo", "tayo", "tulad", "tungkol", "una", "walang"])

# REFERNCE: https://www.link-assistant.com/seo-stop-words.html
ENGLISH_STOP_WORDS = frozenset(["a", "able", "about", "above", "abroad", "according", "accordingly", "across", "actually", "adj", "after", "afterwards", "again", "against", "ago", "ahead", "ain't", "all", "allow", "allows", "almost", "alone", "along", "alongside", "already", "also", "although", "always", "am", "amid", "amidst", "among", "amongst", "an", "and", "another", "any", "anybody", "anyhow", "anyone", "anything", "anyway", "anyways", "anywhere", "apart", "appear", "appreciate", "appropriate", "are", "aren't", "around", "as", "a's", "aside", "ask", "asking", "associated", "at", "available", "away", "awfully", "b", "back", "backward", "backwards", "be", "became", "because", "become", "becomes", "becoming", "been", "before", "beforehand", "begin", "behind", "being", "believe", "below", "beside", "besides", "best", "better", "between", "beyond", "both", "brief", "but", "by", "c", "came", "can", "cannot", "cant", "can't", "caption", "cause", "causes", "certain", "certainly", "changes", "clearly", "c'mon", "co", "co.", "com", "come", "comes", "concerning", "consequently", "consider", "considering", "contain", "containing", "contains", "corresponding", "could", "couldn't", "course", "c's", "currently", "d", "dare", "daren't", "definitely", "described", "despite", "did", "didn't", "different", "directly", "do", "does", "doesn't", "doing", "done", "don't", "down", "downwards", "during", "e", "each", "edu", "eg", "eight", "eighty", "either", "else", "elsewhere", "end", "ending", "enough", "entirely", "especially", "et", "etc", "even", "ever", "evermore", "every", "everybody", "everyone", "everything", "everywhere", "ex", "exactly", "example", "except", "f", "fairly", "far", "farther", "few", "fewer", "fifth", "first", "five", "followed", "following", "follows", "for", "forever", "former", "formerly", "forth", "forward", "found", "four", "from", "further", "furthermore", "g", "get", "gets", "getting", "given", "gives", "go", "goes", "going", "gone", "got", "gotten", "greetings", "h", "had", "hadn't", "half", "happens", "hardly", "has", "hasn't", "have", "haven't", "having", "he", "he'd", "he'll", "hello", "help", "hence", "her", "here", "hereafter", "hereby", "herein", "here's", "hereupon", "hers", "herself", "he's", "hi", "him", "himself", "his", "hither", "hopefully", "how", "howbeit", "however", "hundred", "i", "i'd", "ie", "if", "ignored", "i'll", "i'm", "immediate", "in", "inasmuch", "inc", "inc.", "indeed", "indicate", "indicated", "indicates", "inner", "inside", "insofar", "instead", "into", "inward", "is", "isn't", "it", "it'd", "it'll", "its", "it's", "itself", "i've", "j", "just", "k", "keep", "keeps", "kept", "know", "known", "knows", "l", "last", "lately", "later", "latter", "latterly", "least", "less", "lest", "let", "let's", "like", "liked", "likely", "likewise", "little", "look", "looking", "looks", "low", "lower", "ltd", "m", "made", "mainly", "make", "makes", "many", "may", "maybe", "mayn't", "me", "mean", "meantime", "meanwhile", "merely", "might", "mightn't", "mine", "minus", "miss", "more", "moreover", "most", "mostly", "mr", "mrs", "much", "must", "mustn't", "my", "myself", "n", "name", "namely", "nd", "near", "nearly", "necessary", "need", "needn't", "needs", "neither", "never", "neverf", "neverless", "nevertheless", "new", "next", "nine", "ninety", "no", "nobody", "non", "none", "nonetheless", "noone", "no-one", "nor", "normally", "not", "nothing", "notwithstanding", "novel", "now", "nowhere", "o", "obviously", "of", "off", "often", "oh", "ok", "okay", "old", "on", "once", "one", "ones", "one's", "only", "onto", "opposite", "or", "other", "others", "otherwise", "ought", "oughtn't", "our", "ours", "ourselves", "out", "outside", "over", "overall", "own", "p", "particular", "particularly", "past", "per", "perhaps", "placed", "please", "plus", "possible", "presumably", "probably", "provided", "provides", "q", "que", "quite", "qv", "r", "rather", "rd", "re", "really", "reasonably", "recent", "recently", "regarding", "regardless", "regards", "relatively", "respectively", "right", "round", "s", "said", "same", "saw", "say", "saying", "says", "second", "secondly", "see", "seeing", "seem", "seemed", "seeming", "seems", "seen", "self", "selves", "sensible", "sent", "serious", "seriously", "seven", "several", "shall", "shan't", "she", "she'd", "she'll", "she's", "should", "shouldn't", "since", "six", "so", "some", "somebody", "someday", "somehow", "someone", "something", "sometime", "sometimes", "somewhat", "somewhere", "soon", "sorry", "specified", "specify", "specifying", "still", "sub", "such", "sup", "sure", "t", "take", "taken", "taking", "tell", "tends", "th", "than", "thank", "thanks", "thanx", "that", "that'll", "thats", "that's", "that've", "the", "their", "theirs", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "there'd", "therefore", "therein", "there'll", "there're", "theres", "there's", "thereupon", "there've", "these", "they", "they'd", "they'll", "they're", "they've", "thing", "things", "think", "third", "thirty", "this", "thorough", "thoroughly", "those", "though", "three", "through", "throughout", "thru", "thus", "till", "to", "together", "too", "took", "toward", "towards", "tried", "tries", "truly", "try", "trying", "t's", "twice", "two", "u", "un", "under", "underneath", "undoing", "unfortunately", "unless", "unlike", "unlikely", "until", "unto", "up", "upon", "upwards", "us", "use", "used", "useful", "uses", "using", "usually", "v", "value", "various", "versus", "very", "via", "viz", "vs", "w", "want", "wants", "was", "wasn't", "way", "we", "we'd", "welcome", "well", "we'll", "went", "were", "we're", "weren't", "we've", "what", "whatever", "what'll", "what's", "what've", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "where's", "whereupon", "wherever", "whether", "which", "whichever", "while", "whilst", "whither", "who", "who'd", "whoever", "whole", "who'll", "whom", "whomever", "who's", "whose", "why", "will", "willing", "wish", "with", "within", "without", "wonder", "won't", "would", "wouldn't", "x", "y", "yes", "yet", "you", "you'd", "you'll", "your", "you're", "yours", "yourself", "yourselves", "you've", "z", "zero"])