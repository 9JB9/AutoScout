import { Link } from "react-router-dom"
import "../css/Home.css"
function Home () {
    
    return (
        <div className="home-content">
            <section className="home-hero">
                {/* doing the hero image with a pseudo element on the css side */}
                <div className="home-hero-info">
                    <h2> Finding Your Next Ride... </h2>
                    <p> Made Easy </p>
                </div>
            </section>
            <div className="home-info">
                <div className="home-info-content">
                    <h3> Live listings near you... </h3>
                    <div>
                        <p> Don't want to travel to narnia to buy a car? </p>
                        <p> That's okay, we finds listings within your distance of choice </p>
                        <p> Listings across Canada & America </p>
                    </div>
                    
                </div>
                <div className="home-info-content">
                    <h3> Easy to use and free </h3>
                    <div>
                        <p> Visual map with listing pop ups makes finding and picking a car easier than ever </p>
                        <p> We include dealership information and essential listing details </p>
                        <p> Found an issue? Contact us at <Link to ="/"> Support Page</Link> </p>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Home