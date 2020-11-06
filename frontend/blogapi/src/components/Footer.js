import React from "react";
import { Typography, makeStyles, Grid } from "@material-ui/core";
import { Link } from "react-router-dom";

const useStyles = makeStyles({
  footer: {
    paddingBottom: 40,
    paddingTop: 40,
    paddingLeft: 100,
    paddingRight: 100,
  },
  copy: {
    paddingTop: 30,
  },
});

const DATA = [
  {
    title: "Nosotros",
    content: ["lorem1", "lorem2", "lorem3", "lorem4", "lorem4"],
  },
  {
    title: "Ayuda",
    content: ["lorem1", "lorem2", "lorem3", "lorem4", "lorem4"],
  },
  {
    title: "Documentación",
    content: ["lorem1", "lorem2", "lorem3", "lorem4", "lorem4"],
  },
];

const Copyright = () => {
  const classes = useStyles();
  return (
    <Typography variant="h6" align="center" className={classes.copy}>
      Todos los derechos reservados @2020
    </Typography>
  );
};

const Enlaces = () => {
  return (
    <>
      <Grid container>
        {DATA.map((item, i) => (
          <Grid item xs={12} sm={4} key={i}>
            <Typography variant="h4" style={{ padding: "20px 0" }}>
              {item.title}
            </Typography>
            {item.content.map((item, i) => (
              <Typography variant="h6" key={i}>
                <Link
                  to="/"
                  style={{
                    color: "#444",
                    fontSize: "16px",
                    padding: "10px 0",
                    textDecoration: "none",
                  }}
                >
                  {item}
                </Link>
              </Typography>
            ))}
          </Grid>
        ))}
      </Grid>
    </>
  );
};

const Footer = () => {
  const classes = useStyles();

  return (
    <>
      <div className={classes.footer}>
        <Enlaces />
        <Copyright />
      </div>
    </>
  );
};

export default Footer;
