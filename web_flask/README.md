# AirBnB clone - Web framework

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/qk3bO45DSY-P4qmdnEX93w" title="What is a Web Framework?" target="_blank">What is a Web Framework?</a> </li>
<li><a href="/rltoken/DCF-0NHTuXLykc1ijX5HVg" title="A Minimal Application" target="_blank">A Minimal Application</a> </li>
<li><a href="/rltoken/mfdHqOmCsS7veXQ3nK6PcQ" title="Routing" target="_blank">Routing</a> (<em>except “HTTP Methods”</em>)</li>
<li><a href="/rltoken/_dU2691FhIZB3lBtSF5nMg" title="Rendering Templates" target="_blank">Rendering Templates</a> </li>
<li><a href="/rltoken/V24BEPWuJb3yPZpOvA3-Zw" title="Synopsis" target="_blank">Synopsis</a> </li>
<li><a href="/rltoken/GKvdWdthYkstOwnDs9LJWg" title="Variables" target="_blank">Variables</a> </li>
<li><a href="/rltoken/qum7hVpPWLaqMZBQCpcRyA" title="Comments" target="_blank">Comments</a> </li>
<li><a href="/rltoken/LxOb-5Fe9bHvx0TguTDY9g" title="Whitespace Control" target="_blank">Whitespace Control</a> </li>
<li><a href="/rltoken/8D9OoDX5cYQOFXUqwAiCNw" title="List of Control Structures" target="_blank">List of Control Structures</a> (<em>read up to “Call”</em>)</li>
<li><a href="/rltoken/OMqE9vlalgkWcT_3fu4Hvg" title="Flask" target="_blank">Flask</a> </li>
<li><a href="/rltoken/L3kYnmfrbc86Asb4JZq0rg" title="Jinja" target="_blank">Jinja</a> </li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/lVg3jl6IEzhNeQiHwhC-Fg" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What is a Web Framework</li>
<li>How to build a web framework with Flask</li>
<li>How to define routes in Flask</li>
<li>What is a route</li>
<li>How to handle variables in a route</li>
<li>What is a template</li>
<li>How to create a HTML response in Flask by using a template</li>
<li>How to create a dynamic template (loops, conditions…)</li>
<li>How to display in HTML data from a MySQL database</li>
</ul>

<h2>Requirements</h2>

<h3>Python Scripts</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/python3</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the pycodestyle (version 2.7.*)</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
<li>All your modules should have documentation (<code>python3 -c 'print(__import__("my_module").__doc__)'</code>)</li>
<li>All your classes should have documentation (<code>python3 -c 'print(__import__("my_module").MyClass.__doc__)'</code>)</li>
<li>All your functions (inside and outside a class) should have documentation (<code>python3 -c 'print(__import__("my_module").my_function.__doc__)'</code> and <code>python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'</code>)</li>
<li>A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)</li>
</ul>

<h3>HTML/CSS Files</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files should end with a new line</li>
<li>A <code>README.md</code> file at the root of the folder of the project is mandatory</li>
<li>Your code should be W3C compliant and validate with <a href="/rltoken/BABHSFrobycuS0xRtRtXVQ" title="W3C-Validator" target="_blank">W3C-Validator</a> (except for jinja template)</li>
<li>All your CSS files should be in the <code>styles</code> folder</li>
<li>All your images should be in the <code>images</code> folder</li>
<li>You are not allowed to use <code>!important</code> or <code>id</code> (<code>#...</code> in the CSS file)</li>
<li>All tags must be in uppercase</li>
<li>Current screenshots have been done on <code>Chrome 56.0.2924.87</code>. </li>
<li>No cross browsers </li>
</ul>

<h2>More Info</h2>

<h3>MySQL Default charset issues</h3>

<ul>
<li>If you get Flask errors after executing the  <code>curl ...</code> commands, it might be because of the <code>DEFAULT CHARSET</code>. If it’s <code>DEFAULT CHARSET=latam1</code>, you might want to change it to <code>DEFAULT CHARSET=utf8mb4</code>, either on the server’s config file (/etc/mysql/my.cnf commonly) orm on the CREATE DATABASE statement.</li>
</ul>

<h3>Install Flask</h3>

<pre><code>$ pip3 install Flask
</code></pre>

<p><img src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/concepts/74/hbnb_step3.png" alt="" loading="lazy" style=""></p>

<iframe width="560" height="315" src="https://www.youtube.com/embed/lzs4nQOiZQY" frameborder="0" allowfullscreen=""></iframe>

<h3>NOTE:</h3>

<ul>
<li>Try setting FLASK configuration <code>debug</code> to <code>False</code>  iIf you get the following error when running the checker:</li>
</ul>

<pre><code> - [Got]
rpc error: code = 2 desc = oci runtime error: exec failed: container_linux.go:290: starting container process caused "process_linux.go:111: decoding init error from pipe caused \"read parent: connection reset by peer\""


(222 chars long)
</code></pre>

<h3>Manual QA Review</h3>

<p><strong>It is your responsibility to request a review for this project from a peer before the project’s deadline. If no peers have been reviewed, you should request a review from a TA or staff member.</strong></p>


<details>
<summary>Click to see: Tasks</summary>

<h3 class="panel-title">
0. Hello Flask!
</h3>

Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>Routes:

<ul>
<li><code>/</code>: display “Hello HBNB!”</li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>

<pre><code>guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.0-hello_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>

<p>In another tab:</p>

<pre><code>guillaume@ubuntu:~$ curl 0.0.0.0:5000 ; echo "" | cat -e
Hello HBNB!$
guillaume@ubuntu:~$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-AirBnB_clone_v2</code></li>
<li>Directory: <code>web_flask</code></li>
<li>File: <code>0-hello_route.py, __init__.py</code></li>
</ul>
</div>

<h3 class="panel-title">
1. HBNB
</h3>

Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>Routes:

<ul>
<li><code>/</code>: display “Hello HBNB!”</li>
<li><code>/hbnb</code>: display “HBNB”</li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>

<pre><code>guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.1-hbnb_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>

<p>In another tab:</p>

<pre><code>guillaume@ubuntu:~$ curl 0.0.0.0:5000/hbnb ; echo "" | cat -e
HBNB$
guillaume@ubuntu:~$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-AirBnB_clone_v2</code></li>
<li>Directory: <code>web_flask</code></li>
<li>File: <code>1-hbnb_route.py</code></li>
</ul>
</div>

<h3 class="panel-title">
2. C is fun!
</h3>

Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>Routes:

<ul>
<li><code>/</code>: display “Hello HBNB!”</li>
<li><code>/hbnb</code>: display “HBNB”</li>
<li><code>/c/<text></code>: display “C ” followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)</li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>

<pre><code>guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.2-c_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>

<p>In another tab:</p>

<pre><code>guillaume@ubuntu:~$ curl 0.0.0.0:5000/c/is_fun ; echo "" | cat -e
C is fun$
guillaume@ubuntu:~$ curl 0.0.0.0:5000/c/cool ; echo "" | cat -e
C cool$
guillaume@ubuntu:~$ curl 0.0.0.0:5000/c
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-AirBnB_clone_v2</code></li>
<li>Directory: <code>web_flask</code></li>
<li>File: <code>2-c_route.py</code></li>
</ul>
</div>

<h3 class="panel-title">
3. Python is cool!
</h3>

Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>Routes:

<ul>
<li><code>/</code>: display “Hello HBNB!”</li>
<li><code>/hbnb</code>: display “HBNB”</li>
<li><code>/c/<text></code>: display “C ”, followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)</li>
<li><code>/python/<text></code>: display “Python ”, followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)

<ul>
<li>The default value of <code>text</code> is “is cool”</li>
</ul></li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>

<pre><code>guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.3-python_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>

<p>In another tab:</p>

<pre><code>guillaume@ubuntu:~$ curl -Ls 0.0.0.0:5000/python/is_magic ; echo "" | cat -e
Python is magic$
guillaume@ubuntu:~$ curl -Ls 0.0.0.0:5000/python ; echo "" | cat -e
Python is cool$
guillaume@ubuntu:~$ curl -Ls 0.0.0.0:5000/python/ ; echo "" | cat -e
Python is cool$
guillaume@ubuntu:~$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-AirBnB_clone_v2</code></li>
<li>Directory: <code>web_flask</code></li>
<li>File: <code>3-python_route.py</code></li>
</ul>
</div>

<h3 class="panel-title">
4. Is it a number?
</h3>

Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>Routes:

<ul>
<li><code>/</code>: display “Hello HBNB!”</li>
<li><code>/hbnb</code>: display “HBNB”</li>
<li><code>/c/<text></code>: display “C ”, followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)</li>
<li><code>/python/<text></code>: display “Python ”, followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)

<ul>
<li>The default value of <code>text</code> is “is cool”</li>
</ul></li>
<li><code>/number/<n></code>: display “<code>n</code> is a number” <strong>only</strong> if <code>n</code> is an integer</li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>

<pre><code>guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.4-number_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>

<p>In another tab:</p>

<pre><code>guillaume@ubuntu:~$ curl 0.0.0.0:5000/number/89 ; echo "" | cat -e
89 is a number$
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number/8.9
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number/python
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-AirBnB_clone_v2</code></li>
<li>Directory: <code>web_flask</code></li>
<li>File: <code>4-number_route.py</code></li>
</ul>
</div>

<h3 class="panel-title">
5. Number template
</h3>

Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>Routes:

<ul>
<li><code>/</code>: display “Hello HBNB!”</li>
<li><code>/hbnb</code>: display “HBNB”</li>
<li><code>/c/<text></code>: display “C ”, followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)</li>
<li><code>/python/<text></code>: display “Python ”, followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)

<ul>
<li>The default value of <code>text</code> is “is cool”</li>
</ul></li>
<li><code>/number/<n></code>: display “<code>n</code> is a number” <strong>only</strong> if <code>n</code> is an integer</li>
<li><code>/number_template/<n></code>: display a HTML page <strong>only</strong> if <code>n</code> is an integer:

<ul>
<li><code>H1</code> tag: “Number: <code>n</code>” inside the tag <code>BODY</code> </li>
</ul></li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>

<pre><code>guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.5-number_template
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>

<p>In another tab:</p>

<pre><code>guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_template/89 ; echo ""
<!DOCTYPE html>
<HTML lang="en">
<HEAD>
<TITLE>HBNB</TITLE>
</HEAD>
<BODY>
<H1>Number: 89</H1>
</BODY>
</HTML>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_template/8.9
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_template/python
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-AirBnB_clone_v2</code></li>
<li>Directory: <code>web_flask</code></li>
<li>File: <code>5-number_template.py, templates/5-number.html</code></li>
</ul>
</div>

<h3 class="panel-title">
6. Odd or even?
</h3>

Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>Routes:

<ul>
<li><code>/</code>: display “Hello HBNB!”</li>
<li><code>/hbnb</code>: display “HBNB”</li>
<li><code>/c/<text></code>: display “C ”, followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)</li>
<li><code>/python/<text></code>: display “Python ”, followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)

<ul>
<li>The default value of <code>text</code> is “is cool”</li>
</ul></li>
<li><code>/number/<n></code>: display “<code>n</code> is a number” <strong>only</strong> if <code>n</code> is an integer</li>
<li><code>/number_template/<n></code>: display a HTML page <strong>only</strong> if <code>n</code> is an integer:

<ul>
<li><code>H1</code> tag: “Number: <code>n</code>” inside the tag <code>BODY</code></li>
</ul></li>
<li><code>/number_odd_or_even/<n></code>: display a HTML page <strong>only</strong> if <code>n</code> is an integer:

<ul>
<li><code>H1</code> tag: “Number: <code>n</code> is <code>even|odd</code>” inside the tag <code>BODY</code></li>
</ul></li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>

<pre><code>guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.6-number_odd_or_even
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>

<p>In another tab:</p>

<pre><code>guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_odd_or_even/89 ; echo ""
<!DOCTYPE html>
<HTML lang="en">
<HEAD>
<TITLE>HBNB</TITLE>
</HEAD>
<BODY>
<H1>Number: 89 is odd</H1>
</BODY>
</HTML>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_odd_or_even/32 ; echo ""
<!DOCTYPE html>
<HTML lang="en">
<HEAD>
<TITLE>HBNB</TITLE>
</HEAD>
<BODY>
<H1>Number: 32 is even</H1>
</BODY>
</HTML>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_odd_or_even/python
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-AirBnB_clone_v2</code></li>
<li>Directory: <code>web_flask</code></li>
<li>File: <code>6-number_odd_or_even.py, templates/6-number_odd_or_even.html</code></li>
</ul>
</div>

<h3 class="panel-title">
7. Improve engines
</h3>

Before using Flask to display our HBNB data, you will need to update some part of our engine:</p>

<p>Update <code>FileStorage</code>: (<code>models/engine/file_storage.py</code>)</p>

<ul>
<li>Add a public method <code>def close(self):</code>: call <code>reload()</code> method for deserializing the JSON file to objects</li>
</ul>

<p>Update <code>DBStorage</code>: (<code>models/engine/db_storage.py</code>)</p>

<ul>
<li>Add a public method <code>def close(self):</code>: call <code>remove()</code> method on the private session attribute (<code>self.__session</code>) <a href="/rltoken/Ev0jeeBWNlaFqPAFe-rZKA" title="tips" target="_blank">tips</a> or <code>close()</code> on the class <code>Session</code> <a href="/rltoken/d7XXqTOZnNCO47YVh5ZziQ" title="tips" target="_blank">tips</a></li>
</ul>

<p>Update <code>State</code>: (<code>models/state.py</code>) - If it’s not already present</p>

<ul>
<li>If your storage engine is not <code>DBStorage</code>, add a public getter method <code>cities</code> to return the list of <code>City</code> objects from <code>storage</code> linked to the current <code>State</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/AirBnB_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3
>>> from models import storage
>>> from models.state import State
>>> len(storage.all(State))
5
>>> len(storage.all(State))
5
>>> # Time to insert new data!
</code></pre>

<p>At this moment, in another tab:</p>

<pre><code>guillaume@ubuntu:~/AirBnB_v2$ echo 'INSERT INTO `states` VALUES ("421a55f1-7d82-45d9-b54c-a76916479545", "Alabama", "2017-03-25 19:42:40","2017-03-25 19:42:40");' | mysql -uroot -p hbnb_dev_db
Enter password:
guillaume@ubuntu:~/AirBnB_v2$
</code></pre>

<p>And let’s go back the Python console:</p>

<pre><code>>>> # Time to insert new data!
>>> len(storage.all(State))
5
>>> # normal: the SQLAlchemy didn't reload his `Session`
>>> # to force it, you must remove the current session to create a new one:
>>> storage.close()
>>> len(storage.all(State))
6
>>> # perfect!
</code></pre>

<p>And for the getter <code>cities</code> in the <code>State</code> model:</p>

<pre><code>guillaume@ubuntu:~/AirBnB_v2$ cat main.py
#!/usr/bin/python3
"""
Test cities access from a state
"""
from models import storage
from models.state import State
from models.city import City

"""
Objects creations
"""
state_1 = State(name="California")
print("New state: {}".format(state_1))
state_1.save()
state_2 = State(name="Arizona")
print("New state: {}".format(state_2))
state_2.save()

city_1_1 = City(state_id=state_1.id, name="Napa")
print("New city: {} in the state: {}".format(city_1_1, state_1))
city_1_1.save()
city_1_2 = City(state_id=state_1.id, name="Sonoma")
print("New city: {} in the state: {}".format(city_1_2, state_1))
city_1_2.save()
city_2_1 = City(state_id=state_2.id, name="Page")
print("New city: {} in the state: {}".format(city_2_1, state_2))
city_2_1.save()


"""
Verification
"""
print("")
all_states = storage.all(State)
for state_id, state in all_states.items():
for city in state.cities:
print("Find the city {} in the state {}".format(city, state))

guillaume@ubuntu:~/AirBnB_v2$
guillaume@ubuntu:~/AirBnB_v2$ rm file.json ; HBNB_TYPE_STORAGE=fs ./main.py
New state: [State] (5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45) {'name': 'California', 'id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 509954), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 509950)}
New state: [State] (a5e5311a-3c19-4995-9485-32c74411b416) {'name': 'Arizona', 'id': 'a5e5311a-3c19-4995-9485-32c74411b416', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510256), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510252)}
New city: [City] (e3e36ded-fe56-44f5-bf08-8a27e2b30672) {'name': 'Napa', 'id': 'e3e36ded-fe56-44f5-bf08-8a27e2b30672', 'state_id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510797), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510791)} in the state: [State] (5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45) {'name': 'California', 'id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510038), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 509950)}
New city: [City] (12a58d70-e255-4c1e-8a68-7d5fb924d2d2) {'name': 'Sonoma', 'id': '12a58d70-e255-4c1e-8a68-7d5fb924d2d2', 'state_id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 511437), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 511432)} in the state: [State] (5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45) {'name': 'California', 'id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510038), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 509950)}
New city: [City] (a693bdb9-e0ca-4521-adfd-e1a93c093b4b) {'name': 'Page', 'id': 'a693bdb9-e0ca-4521-adfd-e1a93c093b4b', 'state_id': 'a5e5311a-3c19-4995-9485-32c74411b416', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 511873), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 511869)} in the state: [State] (a5e5311a-3c19-4995-9485-32c74411b416) {'name': 'Arizona', 'id': 'a5e5311a-3c19-4995-9485-32c74411b416', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510373), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510252)}

Find the city [City] (e3e36ded-fe56-44f5-bf08-8a27e2b30672) {'name': 'Napa', 'id': 'e3e36ded-fe56-44f5-bf08-8a27e2b30672', 'state_id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510953), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510791)} in the state [State] (5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45) {'name': 'California', 'id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510038), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 509950)}
Find the city [City] (12a58d70-e255-4c1e-8a68-7d5fb924d2d2) {'name': 'Sonoma', 'id': '12a58d70-e255-4c1e-8a68-7d5fb924d2d2', 'state_id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 511513), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 511432)} in the state [State] (5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45) {'name': 'California', 'id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510038), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 509950)}
Find the city [City] (a693bdb9-e0ca-4521-adfd-e1a93c093b4b) {'name': 'Page', 'id': 'a693bdb9-e0ca-4521-adfd-e1a93c093b4b', 'state_id': 'a5e5311a-3c19-4995-9485-32c74411b416', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 512073), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 511869)} in the state [State] (a5e5311a-3c19-4995-9485-32c74411b416) {'name': 'Arizona', 'id': 'a5e5311a-3c19-4995-9485-32c74411b416', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510373), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510252)}
guillaume@ubuntu:~/AirBnB_v2$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-AirBnB_clone_v2</code></li>
<li>File: <code>models/engine/file_storage.py, models/engine/db_storage.py, models/state.py</code></li>
</ul>
</div>

<h3 class="panel-title">
8. List of states
</h3>

Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>You must use <code>storage</code> for fetching data from the storage engine (<code>FileStorage</code> or <code>DBStorage</code>) => <code>from models import storage</code> and <code>storage.all(...)</code></li>
<li>After each request you must remove the current SQLAlchemy Session:

<ul>
<li>Declare a method to handle <code>@app.teardown_appcontext</code></li>
<li>Call in this method <code>storage.close()</code></li>
</ul></li>
<li>Routes:

<ul>
<li><code>/states_list</code>: display a HTML page: (inside the tag <code>BODY</code>)

<ul>
<li><code>H1</code> tag: “States”</li>
<li><code>UL</code> tag: with the list of all <code>State</code> objects present in <code>DBStorage</code> <strong>sorted by <code>name</code></strong> (A->Z) <a href="/rltoken/UVC1Bw_-nfa_0T2gv1MuQg" title="tip" target="_blank">tip</a>

<ul>
<li><code>LI</code> tag: description of one <code>State</code>: <code><state.id>: <B><state.name></B></code></li>
</ul></li>
</ul></li>
</ul></li>
<li><strong>NOTE: Students have reported that this one does not work - use the next on instead.</strong> Import this <a href="https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/290/7-states_list.sql" title="7-dump" target="_blank">7-dump</a> to have some data</li>
<li>Import this <a href="https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/290/100-hbnb.sql" title="100-dump" target="_blank">100-dump</a> to have some data</li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>

<p><strong>IMPORTANT</strong></p>

<ul>
<li>Make sure you have a running and valid <code>setup_mysql_dev.sql</code> in your <code>AirBnB_clone_v2</code> repository (<a href="/rltoken/-Sz0UGvAe4_SLfTbSXSbzg" title="Task" target="_blank">Task</a>)</li>
<li>Make sure all tables are created when you run <code>echo "quit" | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/AirBnB_v2$ curl -o 7-dump.sql "https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/290/100-hbnb.sql"
guillaume@ubuntu:~/AirBnB_v2$ cat 7-dump.sql | mysql -uroot -p
Enter password:
guillaume@ubuntu:~/AirBnB_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.7-states_list
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>

<p>In another tab:</p>

<pre><code>guillaume@ubuntu:~$ curl 0.0.0.0:5000/states_list ; echo ""
<!DOCTYPE html>
<HTML lang="en">
<HEAD>
<TITLE>HBNB</TITLE>
</HEAD>
<BODY>
<H1>States</H1>
<UL>

<LI>421a55f4-7d82-47d9-b54c-a76916479545: <B>Alabama</B></LI>

<LI>421a55f4-7d82-47d9-b54c-a76916479546: <B>Arizona</B></LI>

<LI>421a55f4-7d82-47d9-b54c-a76916479547: <B>California</B></LI>

<LI>421a55f4-7d82-47d9-b54c-a76916479548: <B>Colorado</B></LI>

<LI>421a55f4-7d82-47d9-b54c-a76916479549: <B>Florida</B></LI>

<LI>421a55f4-7d82-47d9-b54c-a76916479550: <B>Georgia</B></LI>

<LI>421a55f4-7d82-47d9-b54c-a76916479551: <B>Hawaii</B></LI>

<LI>421a55f4-7d82-47d9-b54c-a76916479552: <B>Illinois</B></LI>

<LI>421a55f4-7d82-47d9-b54c-a76916479553: <B>Indiana</B></LI>

<LI>421a55f4-7d82-47d9-b54c-a76916479554: <B>Louisiana</B></LI>

<LI>421a55f4-7d82-47d9-b54c-a76916479555: <B>Minnesota</B></LI>

<LI>421a55f4-7d82-47d9-b54c-a76916479556: <B>Mississippi</B></LI>

<LI>421a55f4-7d82-47d9-b54c-a76916479557: <B>Oregon</B></LI>

</UL>
</BODY>
</HTML>
guillaume@ubuntu:~$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-AirBnB_clone_v2</code></li>
<li>File: <code>web_flask/7-states_list.py, web_flask/templates/7-states_list.html</code></li>
</ul>
</div>

<h3 class="panel-title">
9. Cities by states
</h3>

Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>You must use <code>storage</code> for fetching data from the storage engine (<code>FileStorage</code> or <code>DBStorage</code>) => <code>from models import storage</code> and <code>storage.all(...)</code></li>
<li>To load all cities of a <code>State</code>:

<ul>
<li>If your storage engine is <code>DBStorage</code>, you must use <code>cities</code> relationship</li>
<li>Otherwise, use the public getter method <code>cities</code></li>
</ul></li>
<li>After each request you must remove the current SQLAlchemy Session:

<ul>
<li>Declare a method to handle <code>@app.teardown_appcontext</code></li>
<li>Call in this method <code>storage.close()</code></li>
</ul></li>
<li>Routes:

<ul>
<li><code>/cities_by_states</code>: display a HTML page: (inside the tag <code>BODY</code>)

<ul>
<li><code>H1</code> tag: “States”</li>
<li><code>UL</code> tag: with the list of all <code>State</code> objects present in <code>DBStorage</code> <strong>sorted by <code>name</code></strong> (A->Z) <a href="/rltoken/UVC1Bw_-nfa_0T2gv1MuQg" title="tip" target="_blank">tip</a>

<ul>
<li><code>LI</code> tag: description of one <code>State</code>: <code><state.id>: <B><state.name></B></code> + <code>UL</code> tag: with the list of <code>City</code> objects linked to the <code>State</code> <strong>sorted by <code>name</code></strong> (A->Z)

<ul>
<li><code>LI</code> tag: description of one <code>City</code>: <code><city.id>: <B><city.name></B></code></li>
</ul></li>
</ul></li>
</ul></li>
</ul></li>
<li><strong>NOTE: Students have reported that this one does not work - use the next on instead.</strong> Import this <a href="https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/290/7-states_list.sql" title="7-dump" target="_blank">7-dump</a> to have some data</li>
<li>Import this <a href="https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/290/100-hbnb.sql" title="100-dump" target="_blank">100-dump</a> to have some data</li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>

<p><strong>IMPORTANT</strong></p>

<ul>
<li>Make sure you have a running and valid <code>setup_mysql_dev.sql</code> in your <code>AirBnB_clone_v2</code> repository (<a href="/rltoken/gIfF4l2eWBO13bfNduSG4w" title="Task" target="_blank">Task</a>)</li>
<li>Make sure all tables are created when you run <code>echo "quit" | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/AirBnB_v2$ curl -o 7-dump.sql "https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/290/100-hbnb.sql"
guillaume@ubuntu:~/AirBnB_v2$ cat 7-dump.sql | mysql -uroot -p
Enter password:
guillaume@ubuntu:~/AirBnB_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.8-cities_by_states
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>

<p>In another tab:</p>

<pre><code>guillaume@ubuntu:~$ curl 0.0.0.0:5000/cities_by_states ; echo ""
<!DOCTYPE html>
<HTML lang="en">
<HEAD>
<TITLE>HBNB</TITLE>
</HEAD>
<BODY>
<H1>States</H1>
<UL>

<LI>421a55f4-7d82-47d9-b54c-a76916479545: <B>Alabama</B>
<UL>

<LI>521a55f4-7d82-47d9-b54c-a76916479545: <B>Akron</B></LI>

<LI>531a55f4-7d82-47d9-b54c-a76916479545: <B>Babbie</B></LI>

<LI>541a55f4-7d82-47d9-b54c-a76916479545: <B>Calera</B></LI>

<LI>551a55f4-7d82-47d9-b54c-a76916479545: <B>Fairfield</B></LI>

</UL>
</LI>

<LI>421a55f4-7d82-47d9-b54c-a76916479546: <B>Arizona</B>
<UL>

<LI>521a55f4-7d82-47d9-b54c-a76916479546: <B>Douglas</B></LI>

<LI>531a55f4-7d82-47d9-b54c-a76916479546: <B>Kearny</B></LI>

<LI>541a55f4-7d82-47d9-b54c-a76916479546: <B>Tempe</B></LI>

</UL>
</LI>

<LI>421a55f4-7d82-47d9-b54c-a76916479547: <B>California</B>
<UL>

<LI>541a55f4-7d82-47d9-b54c-a76916479547: <B>Fremont</B></LI>

<LI>551a55f4-7d82-47d9-b54c-a76916479547: <B>Napa</B></LI>

<LI>521a55f4-7d82-47d9-b54c-a76916479547: <B>San Francisco</B></LI>

<LI>531a55f4-7d82-47d9-b54c-a76916479547: <B>San Jose</B></LI>

<LI>561a55f4-7d82-47d9-b54c-a76916479547: <B>Sonoma</B></LI>

</UL>
</LI>

<LI>421a55f4-7d82-47d9-b54c-a76916479548: <B>Colorado</B>
<UL>

<LI>521a55f4-7d82-47d9-b54c-a76916479548: <B>Denver</B></LI>

</UL>
</LI>

<LI>421a55f4-7d82-47d9-b54c-a76916479549: <B>Florida</B>
<UL>

<LI>521a55f4-7d82-47d9-b54c-a76916479549: <B>Miami</B></LI>

<LI>531a55f4-7d82-47d9-b54c-a76916479549: <B>Orlando</B></LI>

</UL>
</LI>

<LI>421a55f4-7d82-47d9-b54c-a76916479550: <B>Georgia</B>
<UL>

</UL>
</LI>

<LI>421a55f4-7d82-47d9-b54c-a76916479551: <B>Hawaii</B>
<UL>

<LI>521a55f4-7d82-47d9-b54c-a76916479551: <B>Honolulu</B></LI>

<LI>531a55f4-7d82-47d9-b54c-a76916479551: <B>Kailua</B></LI>

<LI>541a55f4-7d82-47d9-b54c-a76916479551: <B>Pearl city</B></LI>

</UL>
</LI>

<LI>421a55f4-7d82-47d9-b54c-a76916479552: <B>Illinois</B>
<UL>

<LI>521a55f4-7d82-47d9-b54c-a76916479552: <B>Chicago</B></LI>

<LI>561a55f4-7d82-47d9-b54c-a76916479552: <B>Joliet</B></LI>

<LI>541a55f4-7d82-47d9-b54c-a76916479552: <B>Naperville</B></LI>

<LI>531a55f4-7d82-47d9-b54c-a76916479552: <B>Peoria</B></LI>

<LI>551a55f4-7d82-47d9-b54c-a76916479552: <B>Urbana</B></LI>

</UL>
</LI>

<LI>421a55f4-7d82-47d9-b54c-a76916479553: <B>Indiana</B>
<UL>

</UL>
</LI>

<LI>421a55f4-7d82-47d9-b54c-a76916479554: <B>Louisiana</B>
<UL>

<LI>531a55f4-7d82-47d9-b54c-a76916479554: <B>Baton rouge</B></LI>

<LI>541a55f4-7d82-47d9-b54c-a76916479554: <B>Lafayette</B></LI>

<LI>521a55f4-7d82-47d9-b54c-a76916479554: <B>New Orleans</B></LI>

</UL>
</LI>

<LI>421a55f4-7d82-47d9-b54c-a76916479555: <B>Minnesota</B>
<UL>

<LI>521a55f4-7d82-47d9-b54c-a76916479555: <B>Saint Paul</B></LI>

</UL>
</LI>

<LI>421a55f4-7d82-47d9-b54c-a76916479556: <B>Mississippi</B>
<UL>

<LI>521a55f4-7d82-47d9-b54c-a76916479556: <B>Jackson</B></LI>

<LI>541a55f4-7d82-47d9-b54c-a76916479556: <B>Meridian</B></LI>

<LI>531a55f4-7d82-47d9-b54c-a76916479556: <B>Tupelo</B></LI>

</UL>
</LI>

<LI>421a55f4-7d82-47d9-b54c-a76916479557: <B>Oregon</B>
<UL>

<LI>531a55f4-7d82-47d9-b54c-a76916479557: <B>Eugene</B></LI>

<LI>521a55f4-7d82-47d9-b54c-a76916479557: <B>Portland</B></LI>

</UL>
</LI>

</UL>
</BODY>
</HTML>
guillaume@ubuntu:~$
</code></pre>

<p><img src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2020/9/9a7ae8155274b17881442200437e8793cf08de48.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20231211%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20231211T061941Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=57cc4d9fcaaa47a88ef07e5ed24d30867a5f9fd3a282ea3b3c94f749d44bcc06" alt="" loading="lazy" style=""></p>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-AirBnB_clone_v2</code></li>
<li>File: <code>web_flask/8-cities_by_states.py, web_flask/templates/8-cities_by_states.html</code></li>
</ul>
</div>

<h3 class="panel-title">
10. States and State
</h3>

Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>You must use <code>storage</code> for fetching data from the storage engine (<code>FileStorage</code> or <code>DBStorage</code>) => <code>from models import storage</code> and <code>storage.all(...)</code></li>
<li>To load all cities of a <code>State</code>:

<ul>
<li>If your storage engine is <code>DBStorage</code>, you must use <code>cities</code> relationship</li>
<li>Otherwise, use the public getter method <code>cities</code></li>
</ul></li>
<li>After each request you must remove the current SQLAlchemy Session:

<ul>
<li>Declare a method to handle <code>@app.teardown_appcontext</code></li>
<li>Call in this method <code>storage.close()</code></li>
</ul></li>
<li>Routes:

<ul>
<li><code>/states</code>: display a HTML page: (inside the tag <code>BODY</code>)

<ul>
<li><code>H1</code> tag: “States”</li>
<li><code>UL</code> tag: with the list of all <code>State</code> objects present in <code>DBStorage</code> <strong>sorted by <code>name</code></strong> (A->Z) <a href="/rltoken/UVC1Bw_-nfa_0T2gv1MuQg" title="tip" target="_blank">tip</a>

<ul>
<li><code>LI</code> tag: description of one <code>State</code>: <code><state.id>: <B><state.name></B></code></li>
</ul></li>
</ul></li>
<li><code>/states/<id></code>: display a HTML page: (inside the tag <code>BODY</code>)

<ul>
<li>If a <code>State</code> object is found with this <code>id</code>:

<ul>
<li><code>H1</code> tag: “State: <state.name>”</state.name></li>
<li><code>H3</code> tag: “Cities:”</li>
<li><code>UL</code> tag: with the list of <code>City</code> objects linked to the <code>State</code> <strong>sorted by <code>name</code></strong> (A->Z)

<ul>
<li><code>LI</code> tag: description of one <code>City</code>: <code><city.id>: <B><city.name></B></code></li>
</ul></li>
</ul></li>
<li>Otherwise:

<ul>
<li><code>H1</code> tag: “Not found!”</li>
</ul></li>
</ul></li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
<li><strong>NOTE: Students have reported that this one does not work - use the next on instead.</strong> Import this <a href="https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/290/7-states_list.sql" title="7-dump" target="_blank">7-dump</a> to have some data</li>
<li>Import this <a href="https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/290/100-hbnb.sql" title="100-dump" target="_blank">100-dump</a> to have some data</li>
</ul>

<p><strong>IMPORTANT</strong></p>

<ul>
<li>Make sure you have a running and valid <code>setup_mysql_dev.sql</code> in your <code>AirBnB_clone_v2</code> repository (<a href="/rltoken/gIfF4l2eWBO13bfNduSG4w" title="Task" target="_blank">Task</a>)</li>
<li>Make sure all tables are created when you run <code>echo "quit" | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/AirBnB_v2$ curl -o 7-dump.sql "https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/290/100-hbnb.sql"
guillaume@ubuntu:~/AirBnB_v2$ cat 7-dump.sql | mysql -uroot -p
Enter password:
guillaume@ubuntu:~/AirBnB_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.9-states
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>

<p>In another tab:</p>

<pre><code>guillaume@ubuntu:~$ curl 0.0.0.0:5000/states ; echo ""
<!DOCTYPE html>
<HTML lang="en">
<HEAD>
<TITLE>HBNB</TITLE>
</HEAD>
<BODY>

<H1>States</H1>
<UL>

<LI>421a55f4-7d82-47d9-b54c-a76916479545: <B>Alabama</B></LI>

<LI>421a55f4-7d82-47d9-b54c-a76916479546: <B>Arizona</B></LI>

<LI>421a55f4-7d82-47d9-b54c-a76916479547: <B>California</B></LI>

<LI>421a55f4-7d82-47d9-b54c-a76916479548: <B>Colorado</B></LI>

<LI>421a55f4-7d82-47d9-b54c-a76916479549: <B>Florida</B></LI>

<LI>421a55f4-7d82-47d9-b54c-a76916479550: <B>Georgia</B></LI>

<LI>421a55f4-7d82-47d9-b54c-a76916479551: <B>Hawaii</B></LI>

<LI>421a55f4-7d82-47d9-b54c-a76916479552: <B>Illinois</B></LI>

<LI>421a55f4-7d82-47d9-b54c-a76916479553: <B>Indiana</B></LI>

<LI>421a55f4-7d82-47d9-b54c-a76916479554: <B>Louisiana</B></LI>

<LI>421a55f4-7d82-47d9-b54c-a76916479555: <B>Minnesota</B></LI>

<LI>421a55f4-7d82-47d9-b54c-a76916479556: <B>Mississippi</B></LI>

<LI>421a55f4-7d82-47d9-b54c-a76916479557: <B>Oregon</B></LI>

</UL>

</BODY>
</HTML>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/states/421a55f4-7d82-47d9-b54c-a76916479552 ; echo ""
<!DOCTYPE html>
<HTML lang="en">
<HEAD>
<TITLE>HBNB</TITLE>
</HEAD>
<BODY>

<H1>State: Illinois</H1>
<H3>Cities:</H3>
<UL>
<LI>521a55f4-7d82-47d9-b54c-a76916479552: <B>Chicago</B></LI>

<LI>561a55f4-7d82-47d9-b54c-a76916479552: <B>Joliet</B></LI>

<LI>541a55f4-7d82-47d9-b54c-a76916479552: <B>Naperville</B></LI>

<LI>531a55f4-7d82-47d9-b54c-a76916479552: <B>Peoria</B></LI>

<LI>551a55f4-7d82-47d9-b54c-a76916479552: <B>Urbana</B></LI>
</UL>

</BODY>
</HTML>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/states/holberton ; echo ""
<!DOCTYPE html>
<HTML lang="en">
<HEAD>
<TITLE>HBNB</TITLE>
</HEAD>
<BODY>

<H1>Not found!</H1>

</BODY>
</HTML>
guillaume@ubuntu:~$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-AirBnB_clone_v2</code></li>
<li>File: <code>web_flask/9-states.py, web_flask/templates/9-states.html</code></li>
</ul>
</div>

<h3 class="panel-title">
11. HBNB filters
</h3>

Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>You must use <code>storage</code> for fetching data from the storage engine (<code>FileStorage</code> or <code>DBStorage</code>) => <code>from models import storage</code> and <code>storage.all(...)</code></li>
<li>To load all cities of a <code>State</code>:

<ul>
<li>If your storage engine is <code>DBStorage</code>, you must use <code>cities</code> relationship</li>
<li>Otherwise, use the public getter method <code>cities</code></li>
</ul></li>
<li>After each request you must remove the current SQLAlchemy Session:

<ul>
<li>Declare a method to handle <code>@app.teardown_appcontext</code></li>
<li>Call in this method <code>storage.close()</code></li>
</ul></li>
<li>Routes:

<ul>
<li><code>/hbnb_filters</code>: display a HTML page like <code>6-index.html</code>, which was done during the project <a href="/rltoken/LSsy0WYsMdxl-zlZqbAthg" title="0x01. AirBnB clone - Web static" target="_blank">0x01. AirBnB clone - Web static</a>

<ul>
<li>Copy files <code>3-footer.css</code>, <code>3-header.css</code>, <code>4-common.css</code> and <code>6-filters.css</code> from <code>web_static/styles/</code> to the folder <code>web_flask/static/styles</code></li>
<li>Copy files <code>icon.png</code> and <code>logo.png</code> from <code>web_static/images/</code> to the folder <code>web_flask/static/images</code></li>
<li>Update <code>.popover</code> class in <code>6-filters.css</code> to allow scrolling in the popover and a max height of 300 pixels.</li>
<li>Use <code>6-index.html</code> content as source code for the template <code>10-hbnb_filters.html</code>:

<ul>
<li>Replace the content of the <code>H4</code> tag under each filter title (<code>H3</code> States and <code>H3</code> Amenities) by <code>&nbsp;</code></li>
</ul></li>
<li><code>State</code>, <code>City</code> and <code>Amenity</code> objects must be loaded from <code>DBStorage</code> and <strong>sorted by name</strong> (A->Z)</li>
</ul></li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
<li>Import this <a href="https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/290/10-hbnb_filters.sql" title="10-dump" target="_blank">10-dump</a> to have some data</li>
</ul>

<p><strong>IMPORTANT</strong></p>

<ul>
<li>Make sure you have a running and valid <code>setup_mysql_dev.sql</code> in your <code>AirBnB_clone_v2</code> repository (<a href="/rltoken/gIfF4l2eWBO13bfNduSG4w" title="Task" target="_blank">Task</a>)</li>
<li>Make sure all tables are created when you run <code>echo "quit" | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/AirBnB_v2$ curl -o 10-dump.sql "https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/290/10-hbnb_filters.sql"
guillaume@ubuntu:~/AirBnB_v2$ cat 10-dump.sql | mysql -uroot -p
Enter password:
guillaume@ubuntu:~/AirBnB_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.10-hbnb_filters
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>

<p>In the browser:</p>

<p><img src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2020/9/4f993ec8ca2a2f639a80887667106ac63a0a3701.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20231211%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20231211T061941Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=b38cb283116e19862ffedd792d430f63a59dec2ba6a3397dfe533142b3dde829" alt="" loading="lazy" style="">
<img src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2020/9/1549b553d726cc37f64440be910cb6b858aa32ae.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20231211%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20231211T061941Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=0912e3082a411357922641d92f1d909071a13dab04cc6e7912f577d86eae3eb8" alt="" loading="lazy" style="">
<img src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2020/9/94b3a416ba1551c59701eb6672ac0a36fbebba14.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20231211%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20231211T061941Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=3b0baca0dfd6a2275d0209770cfc64fcf0500e803d1262124fa14c7a756696cf" alt="" loading="lazy" style="">
<img src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2020/9/1e559707dd34a37564dc10e54b707815a516d363.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20231211%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20231211T061941Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=afcdcf0af30c2c0abedf74ac1cd22947ac1b1fa751348f4f92f51a9ce81fc284" alt="" loading="lazy" style=""></p>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-AirBnB_clone_v2</code></li>
<li>File: <code>web_flask/10-hbnb_filters.py, web_flask/templates/10-hbnb_filters.html, web_flask/static/</code></li>
</ul>
</div>

</details>
