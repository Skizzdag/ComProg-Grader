#08_​Texting
texting = {"a":"2","2":"a","b":"22","22":"b","c":"222","222":"c"
           ,"d":"3","3":"d","e":"33","33":"e","f":"333","333":"f"
           ,"g":"4","4":"g","h":"44","44":"h","i":"444","444":"i"
           ,"j":"5","5":"j","k":"55","55":"k","l":"555","555":"l"
           ,"m":"6","6":"m","n":"66","66":"n","o":"666","666":"o"
           ,"t":"8","8":"t","u":"88","88":"u","v":"888","888":"v"
           ,"p":"7","7":"p","q":"77","77":"q","r":"777","777":"r","s":"7777","7777":"s"
           ,"w":"9","9":"w","x":"99","99":"x","y":"999","999":"y","z":"9999","9999":"z"
           ," ":"0","0":" "}
def text2keys(text):
    result = ""
    for i in text.lower():
        if i in texting:
            result += " "+texting[i]
    return result.strip()

def keys2text(keys):
    result = ""
    for i in keys.split():
        if i in texting:
            result += texting[i]
    return result.strip()
exec(input().strip())