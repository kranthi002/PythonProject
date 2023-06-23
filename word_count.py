para = "receiving this email because you registered as kotagirikranthi31@gmail.com. if you don't want to receive these emails in the future, you can unsubscribe from all emails. This email was sent by: Cinemark USA, Inc. 3900 Dallas Parkway • Plano, TX 75093 USA We respect your right to privacy. View our privacy policy."

def word_count(para):
    counts = dict()
    words = para.split()
    
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    
    return counts

print(word_count(para))