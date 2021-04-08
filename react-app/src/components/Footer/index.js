import React from "react";
import { FaLinkedin, FaGithub } from "react-icons/fa";

function Footer(props) {
  return (
    <div className="footer-container">
      <div className="footer-details">
        <img src="" alt="" />
        <a href="https://github.com/laurenchambers" target="_blank">
          <FaGithub />
        </a>
        <a
          href="https://www.linkedin.com/in/lauren-chambers94/"
          target="_blank"
        >
          <FaLinkedin />
        </a>
      </div>
    </div>
  );
}

export default Footer;
