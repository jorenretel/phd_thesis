# coding=utf-8
import re

elements = ['H', 'N', 'C', 'O']

greek_letters = ['alpha', 'beta', 'gamma',]


shouldMatch = ['Halpha', 'H-alpha', 'alpha-helix']
shouldNotMatch = ['alphabet', 'malphar']

shouldMatch = ['13C']
shouldNotMatch = ['13']

findAndReplacePairs = ('13C', )

findAndReplacePairs = [('alpha', 'α'),
                       ('beta', '...'),
                       ('13C', '^13^C'),
                       ('15N', '^15^N'),
                       ('1H', '^1^H'),
                       ('2H', '^2^H'),
                       ]
        
#r'([^\\\b]|[HNCO])(alpha)\b'
 
 
# '\g<1>α'

#greekLetterRegexTemplate = r'(\b|[HNCO])({letter})\b'

greekLetterRegexTemplate = r'(?<!\\)\b([HNCO]?)({letter})\b'

smallGreek= [   ('α', 'alpha'),
                ('β', 'beta'),
                ('γ', 'gamma'),
                ('δ', 'delta'),
                ('ε', 'epsilon'),
                ('ζ', 'zeta'),
                ('η', 'eta'),
                ('θ', 'theta'),
                ('ι', 'iota'),
                ('κ', 'kappa'),
                ('λ', 'lambda'),
                ('μ', 'mu'),
                ('ν', 'nu'),
                ('ξ', 'xi'),
                ('ο', 'omicron'),
                ('π', 'pi'),
                ('ρ', 'rho'),
                ('σ', 'sigma'),
                ('τ', 'tau'),
                ('υ', 'upsilon'),
                ('φ', 'phi'),
                ('χ', 'chi'),
                ('ψ', 'psi'),
                ('ω', 'omega')]

bigGreek = [('Α', 'Alpha'),
            ('Β', 'Beta'),
            ('Γ', 'Gamma'),
            ('Δ', 'Delta'),
            ('Ε', 'Epsilon'),
            ('Ζ', 'Zeta'),
            ('Η', 'Eta'),
            ('Θ', 'Theta'),
            ('Ι', 'Iota'),
            ('Κ', 'Kappa'),
            ('Λ', 'Lambda'),
            ('Μ', 'Mu'),
            ('Ν', 'Nu'),
            ('Ξ', 'Xi'),
            ('Ο', 'Omicron'),
            ('Π', 'Pi'),
            ('Ρ', 'Rho'),
            ('Σ', 'Sigma'),
            ('Τ', 'Tau'),
            ('Υ', 'Upsilon'),
            ('Φ', 'Phi'),
            ('Χ', 'Chi'),
            ('Ψ', 'Psi'),
            ('Ω', 'Omega')]

allGreek = smallGreek + bigGreek

greekRegexTuples = [(re.compile(greekLetterRegexTemplate.format(letter=letterName)), greekLetter ) for greekLetter, letterName in allGreek]

#print smallGreekRegexTuples

text = 'Some alpha alphabet Calpa in a alpha-helix'

#print re.sub(smallGreekRegexTuples[0][0], '\g<1>' + smallGreekRegexTuples[0][1], text)

def replaceGreek(string):
    
    for regex, letter in greekRegexTuples:
        
        string = re.sub(regex, '\g<1>' + letter, string)
    print string
    
text = r'\alpha, alpha-helix and beta-sheet not alpabet and betablocker Alpha-Beta aliphatic and also not latex \alpha'

replaceGreek(text)