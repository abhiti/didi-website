import os
def get_all_files(dir_path):
    """
    https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
    """
    onlyfiles = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f)) and 'DS_Store' not in f]
    onlyfiles.sort()
    return onlyfiles


def generate_gallery_html(dir_path, play_name, play_location):
    """
    ['Scene 0 Prologue.jpeg', 'Scene 1 A.jpeg', 'Scene 1 B.jpeg', 'Scene 1 C.jpeg', 'Scene 1 D.jpeg', 'Scene 1 E.jpeg', 'Scene 1 F.jpeg', 'Scene 1 G.jpeg', 'Scene 10 A.jpeg', 'Scene 10 B.jpeg', 'Scene 10 C.jpeg', 'Scene 10 D.jpeg', 'Scene 10 E.jpeg', 'Scene 10 F.jpeg', 'Scene 11 A.jpeg', 'Scene 11 B.jpeg', 'Scene 11 C.jpeg', 'Scene 11 D.jpeg', 'Scene 12 Set Design 2.jpeg', 'Scene 12 Set Design.jpeg', 'Scene 3 A.jpeg', 'Scene 3 B.jpeg', 'Scene 3 C.jpeg', 'Scene 3 D.jpeg', 'Scene 3 E.jpeg', 'Scene 3 F.jpeg', 'Scene 3 G.jpeg', 'Scene 4 A.jpeg', 'Scene 4 B.jpeg', 'Scene 4 C.jpeg', 'Scene 4 D.jpeg', 'Scene 4 E.jpeg', 'Scene 4 F.jpeg', 'Scene 4 G.jpeg', 'Scene 5 A.jpeg', 'Scene 5 B.jpeg', 'Scene 5 C.jpeg', 'Scene 5 D.jpeg', 'Scene 5 E.jpeg', 'Scene 5 F.jpeg', 'Scene 5 G.jpeg', 'Scene 9 A.jpeg']
    """
    list_of_imgs = get_all_files(dir_path=dir_path)
    html = ""
    for img in list_of_imgs:
        name = img.split('.')[0]
        html += '  <div class="image">'+'\n'
        html +='      <img class="image__img" src="'+dir_path+'/'+img+'" alt="'+name+'">'+'\n'
        html +='      <div class="image__overlay image__overlay--primary">'+'\n'
        html +='          <div class="image__title"><i>'+play_name+'</i></div>'+'\n'
        html +='          <p class="image__description">'+'\n'
        html +='              '+play_location+'\n'
        html += '          </p>'+'\n'
        html += '      </div>'+'\n'
        html += '  </div>'+'\n'
        html += '\n'

    return html

# print(get_all_files(dir_path="gallery-images/writing/jyotis-bridge"))
# print(generate_gallery_html(dir_path="gallery-images/writing/jyotis-bridge", play_name="Jyoti's Bridge", play_location='The Studio @ Schapiro (Columbia University)'))
# print(generate_gallery_html(dir_path="gallery-images/writing/ghost-play", play_name="Ghost Play", play_location='Fresh Lime Soda Productions'))

# print(generate_gallery_html(dir_path="gallery-images/directing/bengal-tiger", play_name="Bengal Tiger at the Baghdad Zoo", play_location='Wellesley College Upstage'))
# print(generate_gallery_html(dir_path="gallery-images/directing/guards-at-the-taj", play_name="Guards at the Taj", play_location='Wellesley College Upstage'))

# print(generate_gallery_html(dir_path="gallery-images/acting/stand-up", play_name="Stand Up", play_location='Comedy Club Adams Morgan'),'\n\n\n')
# print(generate_gallery_html(dir_path="gallery-images/acting/for-molly", play_name="For Molly", play_location='Lenfest Center for the Arts'))
# print(generate_gallery_html(dir_path="gallery-images/acting/much-ado-about-nothing", play_name="Much Ado About Nothing", play_location='Wellesley College Shakespeare Society'),'\n\n\n')
# print(generate_gallery_html(dir_path="gallery-images/acting/dumb-show", play_name="Dumb Show", play_location='Wellesley College Upstage'),'\n\n\n')
# print(generate_gallery_html(dir_path="gallery-images/acting/tempest", play_name="The Tempest", play_location='Wellesley College Shakespeare Society'),'\n\n\n')
# print(generate_gallery_html(dir_path="gallery-images/acting/julius-caesar", play_name="Julius Caesar", play_location='Wellesley College Shakespeare Society'),'\n\n\n')
#print(generate_gallery_html(dir_path="gallery-images/writing/nine-ways", play_name="Nine Ways to Plead With a God", play_location='Lenfest Center for the Arts'),'\n\n\n')
#print(generate_gallery_html(dir_path="gallery-images/directing/eight-one-eight-two", play_name="Eight One Eight Two", play_location='The Chain Theatre'),'\n\n\n')
print(generate_gallery_html(dir_path="gallery-images/directing/let-me-speak-2022", play_name="Let Me Speak 2022", play_location='Wellesley College'),'\n\n\n')


# $ cd /Users/abhiti/Dropbox/Family/DidiSite
# $ python3 directory.py > out.html
