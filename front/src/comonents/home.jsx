import React, {useEffect, useState} from "react";

const Home = () => {
    const [data,setData] = useState([])
    const [curr_name,setCurr_name] = useState("")
    const [curr_id,setCurr_id] = useState("")
    const [updateId,setUpdateID] = useState("")
    const [newName,setNewName] = useState("")
    const fetchData = async () => {
        try{
            const response = await fetch("http://localhost:8000/get/")
            const responseData = await response.json();
            setData(responseData.data)
            console.log(responseData.data)
        } catch(err){
            console.log(err)
        }
        
    }
    const saveData = async () => {
        try{
            const response = await fetch("http://localhost:8000/save/",{
                method: 'POST',
                headers:{
                    'Content-Type':'application/json'
                },
                body:JSON.stringify({
                    'name':curr_name,
                    'id_num':curr_id
                })

            })
            const responseData = await response.json();
            setData(responseData.data)
            console.log(responseData.data)
            setCurr_id("")
            setCurr_name("")
        } catch(err){
            console.log(err)
        }
        
    }
    const deleteData = async (id_num) => {
        try{
            const response = await fetch("http://localhost:8000/delete/",{
                method: 'POST',
                headers:{
                    'Content-Type':'application/json'
                },
                body:JSON.stringify({
                    'id_num':id_num
                })

            })
            const responseData = await response.json();
            setData(responseData.data)
            console.log(responseData.data)
            setCurr_id("")
            setCurr_name("")
        } catch(err){
            console.log(err)
        }
        
    }

    const updateData = async (id_num) => {
        try{
            const response = await fetch("http://localhost:8000/update/",{
                method: 'POST',
                headers:{
                    'Content-Type':'application/json'
                },
                body:JSON.stringify({
                    'name':newName,
                    'id_num':id_num
                })

            })
            const responseData = await response.json();
            setData(responseData.data)
            console.log(responseData.data)
            setCurr_id("")
            setCurr_name("")
            setUpdateID("")
            setNewName("")
        } catch(err){
            console.log(err)
        }
        
    }
    const cancel = () => {
        setUpdateID("")
        setNewName("")
    }
    useEffect(()=>{
        fetchData();
    },[])
    useEffect(()=>{
        console.log(updateId)
    },[updateId])
    return (
       <div className="grid"> 
        <p>From Home</p>
        <div className="border border-gray-800 m-10" >
            <div className="flex mb-5 justify-around mt-10 ">
                <input type="text" name = "name" placeholder="Name" className="border p-1 rounded-md "
                value={curr_name}
                onChange={(e)=>{
                    setCurr_name(e.target.value)
                }}
                required
                />
                <input type="number" name = "id_num" placeholder="Id" className="border p-1 rounded-md" 
                value={curr_id}
                onChange={(e)=>{
                    setCurr_id(e.target.value)
                }}
                required
                />
            </div>
            <button  className="bg-black text-white hover:bg-yellow-200 hover:text-black rounded-md p-2 mb-3"
            onClick={()=>saveData()}
            >
                Save
            </button>
        </div>
        <table class="table-auto border-collapse border border-black w-1/2 justify-self-center ">
            <thead>
            <tr>
                <th className="border border-black">Name</th>
                <th className="border border-black">Id</th>
                <th className="border border-black" colSpan={2}>Action</th>
            </tr>
            </thead>
            <tbody>
            {data.map((item)=>(
                <>
                {(updateId==item.id_num)?(
                    <tr>
                        <td className="border"><input type="text" name = "name" placeholder="Name" className="border p-1 rounded-md "
                        value={newName}
                        onChange={(e)=>{
                            setNewName(e.target.value)
                        }}
                        required
                        /></td>
                        <td className="border">{item.id_num}</td>
                        <td className="border">
                            <button 
                            onClick={()=>cancel()}
                            className="hover:underline hover:text-blue-400">Cancel</button>
                        </td>
                        <td className="border">
                            <button 
                            onClick={()=>updateData(item.id_num)}
                            className="hover:underline hover:text-blue-400">Save</button>
                        </td>
                    </tr>

                ):(
                    <tr>
                        <td className="border">{item.name}</td>
                        <td className="border">{item.id_num}</td>
                        <td className="border">
                            <button 
                            onClick={()=>deleteData(item.id_num)}
                            className="hover:underline hover:text-blue-400">Delete</button>
                        </td>
                        <td className="border">
                            <button 
                            onClick={()=>setUpdateID(item.id_num)}
                            className="hover:underline hover:text-blue-400">Update</button>
                        </td>
                    </tr>
                )}
                </>
               
            ))}
            </tbody>
        </table>
      
        </div>
    )
}

export default Home;