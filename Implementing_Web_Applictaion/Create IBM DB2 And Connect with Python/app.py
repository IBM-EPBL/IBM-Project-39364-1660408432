from flask import *
import os
import ibm_db_dbi as ibm_db


print('[CONNECTING]')
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=815fa4db-dc03-4c70-869a-a9cc13f33084.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=30367;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;PROTOCOL=TCPIP;UID=hjf40312;PWD=gJEiRbvtOp6RkoMg;",'','')
print('[CONNECTED]')

app = Flask(__name__)
app.secret_key = "dsfaj38uhg9q384h9a84"


@app.route("/")
def index():
    if(conn!=False):
        return "IBM DB2 Connected"
    else:
        return "IBM DB2 failed to connect"

    
if __name__ == "__main__":
    app.run()