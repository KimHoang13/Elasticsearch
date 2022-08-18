<h1 style="text-align:center"><a href="https://fit.dhcn.vn">FIT - HaUI</a></h1>
<h2><b>Install Elasticsearch</b></h2>
<p><i>ROOT</i></p>
<h3><b>1. Install OpenJDK java:</b></h3>
<p><code>dnf install java-11-openjdk</code></p>
<p><code>java -version //check java version</code></p>
<hr/>
<h3><b>2. Download and Install the Public Signing Key:</b></h3>
<div>
    <p><code>rpm --import https://artifacts.elastic.co/GPG-KEY-elasticsearch</code></p>
</div>
<hr/>
<h3><b>3. Create and add Elasticsearch repository for yum / dnf:</b></h3>
<div>
    <p><code>tee /etc/yum.repos.d/elasticsearch.repo && EOF</code></p>
    <p><code>Repo.txt</code></p>
    <p><code>EOF</code></p>
</div>
<hr/>
<h3><b>4. Install Elasticsearch:</b></h3>
<div>
    <p><code>dnf install --assumeyes elasticsearch</code></p>
</div>
<hr/>
<h3><b>5. Elasticsearch configuration</b></h3>
<div>
    <p><code>vi /etc/elasticsearch/elasticsearch.yml</code></p>
    <p><i>network.host: localhost</i></p>
</div>
<div>
    <p><code>nano /etc/elasticsearch/jvm.options</code></p>
    <p><i>-Xms2g<br/>
        -Xmx2g</i></p>
</div>
<hr/>
<h3><b>6.Open Elasticsearch</b></h3>
<div>
    <p><code>service elasticsearch start</code></p>
</div>
<hr/>
<h3><b>7. Mapping</b></h3>
<div>
    <p><i>Mapping.txt</i></p>
</div>
<hr/>
<h3><b>8. Start</b></h3>
<div>
    <p><code>service elasticsearch start</code></p>
</div>
<hr/>
<h3><b>9. Check</b></h3>
<div>
    <p><i>browser : localhost:9200</i></p>
    <p><code>service elasticsearch status</code></p>
    <p><code>curl -X GET "localhost:9200/?pretty"</code></p>
    <p><code>curl 'localhost:9200/_cat/indices?v' --user ':'</code></p>
</div>
<hr/>