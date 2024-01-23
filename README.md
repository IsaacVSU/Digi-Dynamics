# Digi-Dynamics
Database system class with 
- Hunter Smith
- Alfred Newsome
- Isaac Watts

# HOW TO RUN
<a href="https://docs.djangoproject.com/en/5.0/">https://docs.djangoproject.com/en/5.0/ </a>
<ol>
  <li>Check version:</li>
  ```
  python -m django --version
  ```
  <li>Use Django to start a project</li>
  ```
  django-admin startproject mysite
  ```
  or if that doesn't work use  
  ```
  python -m django-admin startproject mysite
  ```
  <li>Run django</li>
  ```
  python manage.py runserver
  ```
  <li>Put this URL into the page</li>
  <a href = "http://127.0.0.1:8000/">http://127.0.0.1:8000/</a>
</ol>
# TODO
- [x] Decide On Final Project Plan
- [x] Added a steam web API
- [ ] Apply steam web API with a database
- [ ] Figure out the schema of steam game market

# Types from steam web API
<ul>
  <li>Game</li>
  <li>Music</li>
  <li>Demo</li>
  <li>DLC</li>
</ul>

# Database
<b>Schema</b>
<table>
  <tr>
    <th>Name</th>
    <th>DLC</th>
    <th>Microtransations</th>
    <th>Subsriptions</th>
    <th>Franchise</th>
    <th>Base_price</th>
    <th>Current_Price</th>
    <th>Country</th>
    <th>Developer </th>
    <th>Publisher</th>
    <th>Genre</th>
    <th>Rating</th>
    <th>Review</th>
    <th>Release_data</th>
    <th>Top Seller</th>
    <th>ControllerSupport</th>
    <th>Images</th>
    <th>Trailers</th>
    <th> *Platform</tr>
    <th> *languages </th>
    <th> *tags </th>
  </tr>
</table>
- Note: Any thing with a * may be an issue

```
PrimaryKey: ?
CompositeKey: ?
ForeignKey: ?
```
# Project Ideas
- [x] Steam Game Market
