CONTACT_DETAIL = '''
 <div class="row mb-5">
    <div class="col-sm-8 offset-sm-2">
      <h2>Adresimiz</h2>
      <address>
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Tenetur sequi atque quo quis eligendi temporibus, recusandae voluptatibus nihil amet provident!</p>
      </address>
      <hr />
      <h2 class="mt-5">Bizimle Elaqe Saxlayin</h2>
      <form class="row g-3">
        <div class="row g-3">
          <div class="col">
            <input type="text" class="form-control" placeholder="Ad" aria-label="Ad" />
          </div>
          <div class="col">
            <input type="text" class="form-control" placeholder="Soyad" aria-label="Soyad" />
          </div>
        </div>
        <div class="col-12">
          <label for="inputAddress" class="form-label">Seher/Rayon</label>
          <input type="text" class="form-control" id="inputAddress" />
        </div>
        <div class="col-12">
          <label for="inputEmail4" class="form-label">Email</label>
          <input type="email" class="form-control" id="inputEmail4" />
        </div>
        <div class="col-12">
          <label for="Aciqlama" class="form-label">Aciqlama</label>
          <textarea class="form-control" placeholder="Bura yazin..." id="floatingTextarea"></textarea>
        </div>
        <div class="col-12">
          <label for="inputState" class="form-label">Bizi Nece Tapdiniz?</label>
          <select id="inputState" class="form-select">
            <option selected>Secin...</option>
            <option>Sosial Shebeke</option>
            <option>Radio Reklami</option>
            <option>TV Reklami</option>
            <option>Facebook</option>
            <option>Twitter</option>
            <option>Instagram</option>
          </select>
        </div>

        <div class="col-12">
          <button type="submit" class="btn btn-primary">Gonder</button>
        </div>
      </form>
    </div> 
</div> 
'''

FAKE_DB_PAGES = [
    {"url": "contact", "detail": CONTACT_DETAIL},
    {"url": "info", "detail": CONTACT_DETAIL},
]
