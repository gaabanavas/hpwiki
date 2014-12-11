import re

our_text = "Harry James Potter (b. 31 July, 1980) was a half-blood wizard, the only child and son of James and Lily Potter (née Evans), and one of the most famous wizards of modern times. In what proved to be a vain attempt to circumvent a prophecy, that stated a boy born at the end of July of 1980 could be able to defeat him, Lord Voldemort attempted to murder him when he was a year and three months old, shortly after murdering Harry's parents as they tried to protect him. This early, unsuccessful attempt to vanquish Harry led to Voldemort's first defeat and the end of the First Wizarding War. One consequence of Lily's sacrificial protection is that her orphaned son had to be raised by her only remaining blood relative, Petunia Dursley, where he was neither welcomed nor nurtured, but would stay alive, at least until he was seventeen years old. As the only known survivor of the Killing Curse (up to that point) Harry was already famous before he arrived at Hogwarts School of Witchcraft and Wizardry."
p = re.compile ('[0-9]{4}')
m = p.search(our_text)
print(m.group(0))
