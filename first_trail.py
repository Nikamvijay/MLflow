import mlflow

def calculate_sum(x,y):
    return x+y



if __name__=='__main__':
    """
    staring the server of mlflow
    """
    with mlflow.start_run():
        x,y=10,20
        z=calculate_sum(x,y)  # tracking the expriment with the mlflow
        mlflow.log_param('x',x)
        mlflow.log_param('y',y)
        mlflow.metric('z',z)