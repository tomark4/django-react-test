import React, {useState, useEffect } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardActionArea from '@material-ui/core/CardActionArea';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import Grid from '@material-ui/core/Grid'
import Container from '@material-ui/core/Container'

const URL = 'http://localhost:8000';

const useStyles = makeStyles({
  root: {
    maxWidth: 345,
  },
  loader: {
    margin: "50px 0",
    textAlign: "center"
  }
});

const Loading = () => {
  const classes = useStyles();
  return (
    <>
      <Container className={classes.loader}>
        <Typography variant="h3">Cargando...</Typography>
      </Container>
    </>
  )
}

const Item = ({post}) => {
  const classes = useStyles();

  return (
    <Card className={classes.root}>
      <CardActionArea>
        <CardMedia
          component="img"
          alt="Contemplative Reptile"
          height="300"
          image="https://via.placeholder.com/300"
          title="Contemplative Reptile"
        />
        <CardContent>
          <Typography gutterBottom variant="h5" component="h2">
            {post.id} - {post.title}
          </Typography>
          <Typography variant="body2" color="textSecondary" component="p">
            {post.excerpt}
          </Typography>
        </CardContent>
      </CardActionArea>
      <CardActions>
        <Button size="small" color="primary">
          Share
        </Button>
        <Button size="small" color="primary">
          Learn More
        </Button>
      </CardActions>
    </Card>
  );
}

function Post(){
  const [posts, setPosts] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect( () => {
    const getData = () => {
      fetch(`${URL}/api`)
      .then( resp => resp.json() )
      .then( data => {
        setPosts(data);
        setLoading(false)
      });
    }
    setTimeout( () => {
      getData();
    }, 1500)
  }, []);

  if (loading){
    return <Loading />
  }

  return (
    <>
      <Container>
        <Typography variant="h3" style={{ margin: "20px 0"}}>Our posts</Typography>
        <Grid container>
            { posts.map( post => (
              <Grid item xs={4} key={post.id} style={{ margin:'15px 0'}}>
                <Item post={post} />
              </Grid>
            ))}
        </Grid>
      </Container>
    </>
  )
}


export default Post;
