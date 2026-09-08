import { Link } from "react-router-dom"
import "../css/NavBar.css"

function NavBar() {

    return (
        <nav>
            <Link to = "/" className="nav-left">
                <h1>AutoScout</h1>
            </Link>
            <div className="nav-right">
                <Link to="/login"> Login </Link>
                <Link to="/signup"> Signup </Link>
            </div>
        </nav>
    )
}

export default NavBar