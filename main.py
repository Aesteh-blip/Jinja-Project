from flask import Flask
import random
import string

app = Flask(__name__)

facts_list = [
    "Kebanyakan orang yang menderita kecanduan teknologi mengalami stres yang kuat ketika berada di luar area jangkauan jaringan atau tidak dapat menggunakan perangkat mereka.",
    "Menurut sebuah studi yang dilakukan pada tahun 2018, lebih dari 50% orang berusia 18 hingga 34 tahun menganggap diri mereka bergantung pada ponsel pintar mereka.",
    "Studi tentang ketergantungan teknologi adalah salah satu bidang penelitian ilmiah modern yang paling relevan.",
    "Menurut sebuah studi tahun 2019, lebih dari 60% orang merespons pesan pekerjaan di ponsel mereka dalam waktu 15 menit setelah pulang kerja.",
    "Salah satu cara untuk memerangi ketergantungan teknologi adalah dengan mencari kegiatan yang membawa kesenangan dan meningkatkan suasana hati.",
    "Elon Musk mengklaim bahwa jejaring sosial dirancang untuk membuat kita tetap berada di dalam platform, sehingga kita menghabiskan waktu sebanyak mungkin untuk melihat konten.",
    "Elon Musk juga menganjurkan regulasi jejaring sosial dan perlindungan data pribadi pengguna.",
    "Jejaring sosial memiliki sisi positif dan negatif, dan kita harus menyadari keduanya saat menggunakan platform ini."
]

@app.route("/")
def hello_world():
    return '''
    <h1>Hi! On this page, you can learn a couple of interesting facts about technological dependencies!</h1>
    <ul>
        <li><a href="/random_fact">view a random fact</a></li>
        <li><a href="/lempar_koin">main lempar koin</a></li>
        <li><a href="/password_generator">buat kata sandi acak</a></li>
    </ul>
    '''

@app.route("/random_fact")
def random_fact():
    return f'''
    <p>{random.choice(facts_list)}</p>
    <a href="/">kembali ke utama?</a>
    '''

@app.route("/lempar_koin")
def lempar_koin():
    hasil = random.choice(["kepala", "ekor"])
    return f'''
    <h1>hasil lempar koinmu:</h1>
    <h2>🪙 {hasil}</h2>
    <a href="/lempar_koin">lempar lagi!</a> | <a href="/">kembali ke utama?</a>
    '''

@app.route("/password_generator")
def password_generator():
    karakter = string.ascii_letters + string.digits
    password_acak = "".join(random.choice(karakter) for i in range(10))
    return f'''
    <h1>generator kata sandi acak:</h1>
    <h2>🔒 <code>{password_acak}</code></h2>
    <a href="/password_generator">buat baru!</a> | <a href="/">kembali ke utama?</a>
    '''

if __name__ == "__main__":
    app.run(debug=True)