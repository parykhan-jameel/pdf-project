import React, {useState} from "react";
import axios from "axios";

const UploadForm = () => {
    const [file, setFile] = useState(null);
    const [status, setStatus] = useState('');
    const [fileName, setFileName] = useState('');

    const handleFileChange = (e) => {
        setFile(e.target.files[0])
        if (file) {
          setFileName(file.name)
        }
    }

    const handleUpload = async () => {
        if (!file) {
            alert('Please select a file')
            return
        }

        const formData = new FormData()
          formData.append("title", "Test Title"); 
          formData.append("file", file);

        try {
            setStatus("Uploading...")
            const response = await axios.post('http://127.0.0.1:8000/upload/', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
        })
        setStatus("File uploaded successfully")
        console.log(response.data)
    }
    catch (error) {
        setStatus("Error uploading file")
    }
}
return (
    <div className="max-w-md mx-auto mt-10 p-4 border rounded shadow">
      <h2 className="text-xl font-semibold mb-4">Upload PDF</h2>
      <input
        type="file"
        accept="application/pdf"
        id="file-upload"
        onChange={handleFileChange}
        className="file-input"
      />
      <label
        htmlFor="file-upload"
        className="file-label mb-2"
        style={{ width: '100%', backgroundColor: 'white', border: '1px solid #ddd', padding: '10px', textAlign: 'center', cursor: 'pointer', display: 'inline-block', borderRadius: '5px' }}
      >
        {fileName ? fileName : 'Choose file'}
      </label>
      <button
        onClick={handleUpload}
        className="w-full bg-blue-500 text-white py-2 rounded hover:bg-blue-600"
      >
        Upload
      </button>
      {status && <p className="mt-4">{status}</p>}
    </div>
)

};
export default UploadForm;