import React, {useState} from 'react'

export default function Home(){
  const [file, setFile] = useState(null)
  const upload = async ()=>{
    if(!file) return alert('select file')
    const fd = new FormData();
    fd.append('file', file)
    const res = await fetch('http://localhost:8000/sessions/upload', {method:'POST', body: fd})
    const j = await res.json();
    alert('uploaded: '+ JSON.stringify(j))
  }
  return (
    <div style={{padding:40}}>
      <h1>Therapy Copilot (Dev)</h1>
      <input type='file' onChange={e=>setFile(e.target.files[0])} />
      <button onClick={upload}>Upload</button>
    </div>
  )
}
