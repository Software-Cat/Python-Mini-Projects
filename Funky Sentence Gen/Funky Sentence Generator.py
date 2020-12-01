import random
adjectives = ["abandoned", "baffled", "cringy", "dazzling", "eccentric", "fancy", "generous", "happy", "ill", "jocose", "kind", "lazy", "magical", "naked",
              "obstinate", "patriotic", "queasy", "raging", "savage", "talented", "unlucky", "vegetarian", "white", "xenophobic", "yawning", "zippy"]

executerNouns = ["apple", "banana", "cat", "dog", "elephatnt", "flamingo", "giraffe", "hippo", "iguana", "jellyfish", "kangaroo", "ladybug", "mammoth", "numbat",
                 "octopus", "panda", "quail", "rabbit", "snake", "teacher", "umpire", "vocalist", "whale", "xylophone", "yoga instructor", "zoologist"]

adverbs = ["accidentally", "beneficially", "chaotically", "doubtfully", "efficiently", "fearfullly", "gently", "hypocritically", "impulsively", "jealously", "keenly",
           "loudly", "mysteriously", "naively", "obediently", "passionately", "quietly", "rationally", "sadly", "telepathically", "uncontrollably", "viciously",
           "wildly", "xenophobically", "youthfully", "zealously"]

verbs = ["ate", "bent", "cleaned", "danced", "educated", "fabricated",
         "grew", "hacked", "immobilized", "jumbled", "kicked"]
genders = ["his", "hers"]
subjectNouns = ["aquarium", "bandana", "cabbage"]
prepositions = ["with", "without", "in front of",
                "behind", "next to", "under", "over"]
objects = ["aeroplane", "broom"]

print("The " + random.choice(adjectives) + " " + random.choice(executerNouns) + " " + random.choice(adverbs) + " " + random.choice(verbs) + " " +
      random.choice(genders) + " " + random.choice(subjectNouns) + " " + random.choice(prepositions) + " a/an " + random.choice(objects) + ".")
