

from flask import Flask, request, send_file, jsonify
import os
from scan import search_pdfs_in_folder
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

@app.route('/process', methods=['POST'])
def process():
    try:
        data = request.json
        
        rank = int(data['rank'])
        category = data['category']
        
        if not rank or not category:
            return jsonify({"error": "Please provide both rank and category"}), 400

        # Process the PDFs and create the Excel file
        output_file = search_pdfs_in_folder(rank, category)
        
        if not output_file:
            return jsonify({"error": "Failed to process the request"}), 500

        # Ensure the file exists before sending it
        if os.path.exists(output_file):
            return send_file(output_file, as_attachment=True, download_name=output_file)
        else:
            return jsonify({"error": "File not found"}), 500
    except ValueError:
        return jsonify({"error": "Invalid rank provided"}), 400

if __name__ == '__main__':
        app.run(debug=True)
