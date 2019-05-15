<!DOCTYPE html>
<html>
<head>
</head>
<body>
  <h1>Flask RESTful API + Docker</h1>
  <h3>About</h3>
  <p>An example of using Python Flask to create a REST API in a Docker container.</p>
  <h3>Files</h3>
  <p>
    <ul>
      <li><i>api.py</i> contains the code for the API</li>
      <li><i>Dockerfile</i> contains the instructions/commands needed to build a docker image</li>
      <li><i>requirements.txt</i> contains a list of required Python packages/libraries</li>
    </ul>
  </p>
  <h3>Docker Image</h3>
  <ol>
    <li>Run the command <code class="inlinecode">docker pull fjemilohun/docker_flask_example</code> to download the Docker image</li>
    <li>Run the command <code class="inlinecode">docker run -d -p 8000:5000 mtngt/my_docker_flask:latest</code></li>
    <li>Open a browser and go to http://127.0.0.1:8000/ or use <code class="inlinecode">curl http://127.0.0.1:8000/</code> to do a get request</li>
  </ol>
  <h3>API Paramters</h3>
  <table>
    <col>
    <col>
    <col>
    <col>
    <tr>
      <th scope="col" rowspan="1">URL</th>
      <th scope="col" rowspan="1">Method</th>
      <th scope="col" rowspan="1">Params</th>
      <th scope="col" rowspan="1">Description</th>
    </tr>
    <tr>
      <th scope="row">/</th>
      <td>GET</td>
      <td>None</td>
      <td>Returns <code class="inlinecode">Hello World</code></td>
    </tr>
    <tr>
      <th scope="row">/date</th>
      <td>GET</td>
      <td>None</td>
      <td>Returns current Date (<code class="inlinecode">mm-dd-yy</code>) and Time (<code class="inlinecode">hh:mm:ss</code>)</td>
    </tr>
    <tr>
      <th scope="row">/message=<code class="inlinecode">MESSAGE</code></th>
      <td>GET</td>
      <td>
        <p style="color:#ff0000; font-size:11px;">Required</p>
        <code class="inlinecode">MESSAGE</code> is a string type that must be either <code class="inlinecode">hello</code> or <code class="inlinecode">bye</code>
      </td>
      <td>Returns a greeting or farewell</td>
    </tr>
    <tr>
      <th scope="row">/name=<code class="inlinecode">NAME</code></th>
      <td>GET</td>
      <td>
        <p style="color:#ff0000; font-size:11px;">Required</p>
        <code class="inlinecode">NAME</code> is a string type
      </td>
      <td>Returns a greeting for <code class="inlinecode">NAME</code></td>
    </tr> 
    <tr>
      <th scope="row">/last=<code class="inlinecode">LAST</code>&first=<code class="inlinecode">FIRST</code></th>
      <td>GET</td>
      <td>
        <p style="color:#ff0000; font-size:11px;">Required</p>
        <code class="inlinecode">LAST</code> and <code class="inlinecode">FIRST</code> are string types
      </td>
      <td>Returns the full name (<code class="inlinecode">LAST</code> and <code class="inlinecode">FIRST</code>) provided</td>
    </tr>   
    <tr>
      <th scope="row">/os</th>
      <td>GET</td>
      <td>None</td>
      <td>Returns information about the current operating system</td>
    </tr>                                                                                             
  </table>
</body>
</html>
