name_for_userid = {
    382: "Alice",
    950: "Bob",
    590: "Dilbert",
}

def greeting(userid):
    return "Hi %s!" % name_for_userid.get(userid, 'there')


print(greeting(55))
print(name_for_userid.get(590))
